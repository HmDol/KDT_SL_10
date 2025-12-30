def calc_temp_rise_rate(df):
    """
    [수정됨] 모듈별로 그룹화하여 diff() 차이를 계산합니다.
    (데이터가 'module_id', 'timestamp' 순으로 정렬되어 있어야 함)
    """
    df = df.copy()
    
    # 모듈별로 그룹화하여 diff() 계산
    df["temp_rise_rate"] = df.groupby("module_id")["cell_temperature_c"].diff() / 5
    
    # 각 모듈의 첫 번째 행에서 발생하는 NaN을 0으로 채움
    df["temp_rise_rate"] = df["temp_rise_rate"].fillna(0)
    
    return df


def calc_temp_imbalance(df):
    # (timestamp가 datetime 타입으로 변환되었다고 가정)
    df = df.copy()
    df["temp_imbalance"] = df.groupby("timestamp")["cell_temperature_c"] \
                             .transform(lambda x: x.max() - x.min())
    return df