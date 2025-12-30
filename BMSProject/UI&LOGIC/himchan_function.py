import pandas as pd

def predict_degradation(row):
    """배터리 열화 위험도를 계산하여 0~100 점수 반환"""

    risk = 0
    
    # 1) 온도 리스크
    if row['cell_temperature_c'] > 30:
        risk += (row['cell_temperature_c'] - 30) * 2
    
    # 2) SOC 위험 구간  
    if row['soc_pct'] < 25:
        risk += (25 - row['soc_pct']) * 1.5
    elif row['soc_pct'] > 85:
        risk += (row['soc_pct'] - 85) * 1.5
    
    # 3) 전류 변동성 기반 스트레스 (Z-score 활용)
    # 전류 값이 극단적이면 위험 증가 (실시간 기준)
    if abs(row['module_current_a']) > 22: 
        risk += (abs(row['module_current_a']) - 22) * 1.2
    
    # 4) 시스템 anomaly 기반 영향
    risk += row['anomaly_score_pct'] * 0.8

    # 점수 상한 제한
    return min(round(risk, 2), 100)

def detect_abnormal_module(df):
    """모듈별 상태 기반 비정상 여부를 반환"""
    
    abnormal_modules = []

    module_groups = df.groupby('module_id')

    for module, data in module_groups:
        
        soh_mean = data['soh_pct'].mean()
        soh_std = data['soh_pct'].std()
        anomaly_mean = data['anomaly_score_pct'].mean()
        diag_flag_count = data['diagnostic_flag'].sum()
        
        abnormal_condition = (
            soh_mean < (df['soh_pct'].mean() - 2 * df['soh_pct'].std()) or
            anomaly_mean > 20 or
            diag_flag_count > 3
        )
        
        abnormal_modules.append({
            'module_id': module,
            'avg_soh': round(soh_mean, 2),
            'avg_anomaly': round(anomaly_mean, 2),
            'diagnostic_flags': diag_flag_count,
            'status': '⚠️ 비정상' if abnormal_condition else '✅ 정상'
        })

    return abnormal_modules