## 모듈 로딩
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os




### power error, 충/방전/유후 구분 함수화  

def analyze_power_error(
    df,
    curr_eps: float = 1e-3,   # 전류 0 판단 기준
    z_th: float = 3.0,       # z-score 이상치 기준
    diff_mult: float = 3.0,  # diff 기준 이상치 배수
    verbose: bool = True     # True면 print로 이상치 출력
):
    ## 추가되는 컬럼: 'p_expected_kw' , 'power_error_kw' ,'power_error_z', 

    # 그룹별 정렬
    bms_df = df.sort_values(["module_id", "timestamp"]).reset_index(drop=True)

    # 1. 전력 재계산
    bms_df["p_expected_kw"] = (
        bms_df["cell_voltage_v"] * bms_df["module_current_a"] / 1000.0
    )

    # 1. power_error = 실제 측정된 전력 - 기대 전력
    bms_df["power_error_kw"] = bms_df["module_power_kw"] - bms_df["p_expected_kw"]

    # 1. power_error 이상치 탐지 (z-score)
    mu = bms_df["power_error_kw"].mean()
    sigma = bms_df["power_error_kw"].std()

    bms_df["power_error_z"] = (bms_df["power_error_kw"] - mu) / (sigma + 1e-9)

    # 1. HIGH / LOW
    bms_df["is_high_power_error"] = bms_df["power_error_z"] > z_th
    bms_df["is_low_power_error"] = bms_df["power_error_z"] < -z_th

    # 1. JUMP: power_error_diff 기준
    bms_df["power_error_diff"] = bms_df.groupby("module_id")["power_error_kw"].diff()
    diff_sigma = bms_df["power_error_diff"].std()
    diff_th = diff_mult * diff_sigma

    bms_df["is_jump_power_error"] = bms_df["power_error_diff"].abs() > diff_th

    # 1. 이상치 발생 행만 모아두기
    mask_anom = (
        bms_df["is_high_power_error"] |
        bms_df["is_low_power_error"] |
        bms_df["is_jump_power_error"]
    )
    anomalies_df = bms_df[mask_anom].copy()

    # 1. verbose=True면 이상치 출력
    if verbose:
        for idx, row in anomalies_df.iterrows():
            ts = row["timestamp"]
            mid = row["module_id"]
            err = row["power_error_kw"]
            diff_val = row["power_error_diff"]

            if row["is_high_power_error"]:
                print(f"[HIGH_ERROR] {ts} | {mid} | power_error_kw={err:.4f} kW")

            if row["is_low_power_error"]:
                print(f"[LOW_ERROR]  {ts} | {mid} | power_error_kw={err:.4f} kW")

            if row["is_jump_power_error"]:
                print(
                    f"[JUMP_ERROR] {ts} | {mid} | "
                    f"power_error_kw={err:.4f} kW, diff={diff_val:.4f} kW"
                )
    # 2. 충/방전/유휴 구분
    def classify_mode(i):
        if i > curr_eps:
            return "discharge"  # 방전
        elif i < -curr_eps:
            return "charge"     # 충전
        else:
            return "idle"       # 유휴

    bms_df["mode"] = bms_df["module_current_a"].apply(classify_mode)

    return bms_df, anomalies_df  ## anomalies_df는 이상치 컬럼을 반환. power error의 이상치 컬럼임.

