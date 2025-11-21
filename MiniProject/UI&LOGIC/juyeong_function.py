import pandas as pd
def add_charge_efficiency(batDF: pd.DataFrame,
                          power_col: str = "module_power_kw") -> pd.DataFrame:
    """
    energy_input_kwh = power[kW] * (dt_min/60)[h]
    """
    df = batDF.copy()
    # 시간차 [분]
    dt = 5
    # 에너지 입력량 (kWh) = kw * 1시간
    df["energy_input_kwh"] = df[power_col] * (dt / 60.0)

    return df