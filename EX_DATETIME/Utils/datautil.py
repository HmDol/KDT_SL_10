## ----------------------------------------------------------------------
## Data에 관련된 공통된 함수들(예시: 속성 출력 기능 함수....)
## ----------------------------------------------------------------------
import numpy as np
## ----------------------------------------------------------------------
## 함수이름 : print_info
## 함수기능 : DataFrame, Series의 속성 정보 출력
## 매개변수 : obj    - DataFrame, Series 인스턴스
##           name   - DataFrame, Series 의 이름
##           isDF   - DataFrame 여부 [기] True
## 반환결과 : 없음
## ----------------------------------------------------------------------

def print_info(obj, name, isDF=True):
    print(f'\n[{name}]==================')
    print(f'obj.index   : {obj.index}')
    if isDF : print(f'obj.columns : {obj.columns}')
    print(f'obj.shape   : {obj.shape}')
    print(f'obj.ndim    : {obj.ndim}D')
    if isDF :
        print(f'obj.dtypes\n{obj.dtypes}')    
    else : 
        print(f'obj.dtype\n{obj.dtype}')    


## ----------------------------------------------------------------------
## 함수이름 : summary
## 함수기능 : DataFrame, Series의 기본 정보 및 통계값 출력
## 매개변수 : obj       - DataFrame, Series 인스턴스
##           include   - 수치 컬럼 또는 모든 컬럼 설정 [기] None
## 반환결과 : 없음
## ----------------------------------------------------------------------

def summary(obj, include = None) :
    print(obj.head(3))
    obj.info()
    print(obj.describe(include = include))

## ----------------------------------------------------------------------
## 함수이름 : check_unique
## 함수기능 : 컬럼별 고유값, 고유값 개수, 타입 출력 함수
## 매개변수 : obj       - DataFrame 인스턴스
## 반환결과 : 없음
## ----------------------------------------------------------------------
def check_unique(obj) :
    for col in obj.columns :
        print(f'[{col}] ------------------- {obj[col].nunique()} 개수/ {obj[col].dtype}')
        print(f'{obj[col].unique()}')
        print()
        


## ------------------------------------------------------------
# 2) pandas/numpy만으로 Eta-squared(η²) 계산 함수
## ------------------------------------------------------------
## ANOVA(Analysis of Variance : 분산 분석)
## -> 여러 집단의 평균이 같은지 다른지를 검증하는 통계적 기법
## -> 여러 집단의 평균을 비교하기 위해 집단 내 분산과 집단 간 분산 비교
## -> 공식: η² = SS_between / SS_total
## -> 
## 함수기능 : 수치형 컬럼에 대한 범주형 컬럼의 영향 정도 반환
##           
## 함수이름 : eta_squared_np
## 매개변수 : df      : 데이터프레임
##           cat_col : 범주형/텍스트 컬럼
##           num_col : 수치형 컬럼
## 결과반환 : 0 ~ 1 
## ------------------------------------------------------------
def eta_squared_np(df, cat_col, num_col):

    tmp = df[[cat_col, num_col]].dropna()  # 범주/수치 모두 결측 제거
    if tmp.empty:
        return np.nan, np.nan, np.nan, 0
    
    # 수치형 컬럼 값과 전체 평균
    y = tmp[num_col].to_numpy()
    overall_mean = y.mean()

    # 범주형 기준 그룹 평균/크기
    grouped = tmp.groupby(cat_col)[num_col]
    counts = grouped.size().to_numpy()
    means  = grouped.mean().to_numpy()

    # 집단간 제곱합 (SS_between) = Σ n_g * (μ_g - μ)^2
    ss_between = np.sum(counts * (means - overall_mean) ** 2)

    # 총 제곱합 (SS_total) = Σ (y_i - μ)^2
    ss_total   = np.sum((y - overall_mean) ** 2)

    # (선택) 집단내 제곱합 (SS_within) = SS_total - SS_between
    ss_within  = ss_total - ss_between

    ## 수치형 컬럼들 평균 계산
    y = tmp[num_col].to_numpy()
    overall_mean = y.mean()


    eta2 = ss_between / ss_total if ss_total > 0 else np.nan
    return float(eta2), float(ss_between), float(ss_total), int(len(counts))


## ----------------------------------------------------------------
## [2-5] 컬럼별 이상치 데이터 검사 진행 => IQR 사용
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## 함수기능 : IQR기반 이상치 여부 검사 후 결과 반환
## 함수이름 : iqr_outlier_mask
## 매개변수 : sr                <-- series 인스턴스
##           k=1.5            <-- 임계값
## 결과반환 : 이상치 True, 정상 False 반환된 sr반환
## ----------------------------------------------------------------
def iqr_outlier_mask(sr,k=1.5):
    # 오름차순 정렬 후 중앙값, 중앙값 왼쪽부분 중앙값, 오른쪽 부분 중앙값 추출
    q1, q3 = sr.quantile([0.25, 0.75])
    iqr    = q3 - q1
    lower, upper = q1 - k * iqr , q3 + k * iqr
    return (sr<lower) | (sr > upper)



## ----------------------------------------------------------------
## 함수기능 : 이상치 행 추출해서 해당 정보를 반환
## 함수이름 : 
## 매개변수 : 
## 결과반환 : 이상치 행 추출해서 dict 반환
##           {'columns' : 컬럼명, 'index' : 행인데긋 , 'value' : 데이터}
## ----------------------------------------------------------------

def get_outlier_records(dataDF, numeric_cols, k:float = 1.5) :
    ##이상치 행/레코드 정보 저장
    outlier_records = []
    
    ## 컬럼별 이상치 추출 및 정보 저장
    for col in numeric_cols:
        ## 컬럼별 이상치 검사용 마스크
        colSR = dataDF[col]
        mask = iqr_outlier_mask(colSR, k = k)
        
        ## SR에서 1개라도 True 이면 True 반환 : any() < - > all()
        if mask.any():
            for idx in colSR[mask].index.to_list():
                recordDict = {"columns" : col,
                              "index" : int(idx),
                              "value" : float(colSR.loc[idx])}
                outlier_records.append(recordDict)
                
    return outlier_records

## ----------------------------------------------------------------
## 함수 기능 : 컬럼별 이상치 검사 후 시각화
## 함수 이름 : visualize_outliers
## 매개 변수 : dataDF
##            numeric_cols
##            k=1.5 민감도. 데이터의 분포를 고려해 조절
##                  분산이 큰 데이터 : k를 크게 (예 : 2.0~3.0)
##                  -> 너무 많은 정상값이 이상치로 잡히는 걸 방지
##                  - - - - - - - - - - - - - - - - - - - - - - - -
##                  값이 좁은 구간에 밀집된 데이터 : k를 작게 (예:1.0~1.2)
##                  -> 미세한 튀는 점도 포착 가능
## 결과 반환 : 이상치 산점도와 일반 산점도를 동시에 표시
## ----------------------------------------------------------------
def visualize_outliers(dataDF, numeric_cols, k=1.5):
    for col in numeric_cols :
        ## - 컬럼별 이상치 검사
        colSR = dataDF[col]
        mask = iqr_outlier_mask(colSR, k=1.5)
        
        ## 시각화 그래프
        plt.figure(figsize=(7,4))
        ## 모든 데이터 산점도
        plt.scatter(colSR.index, colSR, label=col)
        
        ## 이상치 데이터만 추출해서 산점도 출력
        out_idx = mask[mask].index
        plt.scatter(out_idx, colSR.loc[out_idx], marker='x', s=100, label='outlier')
        
        ## 그래프 공통
        plt.title(f'{col} -- index vs value (IQR)')
        plt.xlabel("index")
        plt.ylabel(col)
        plt.legend()
        plt.tight_layout()
        plt.show()

## ----------------------------------------------------------------
## 함수 기능 : 이상치 치환 후 반환
## 함수 이름 : cap_iqr
## 매개 변수 : SR, k=1.5
## 결과 반환 : 하한값/상한값으로 이상치 치환 후 반환
## ----------------------------------------------------------------
## => 해당 값은 생물학적으로 가능한가?
def cap_iqr(s, k=1.5):
    # 4분위수 계산
    q1, q3 = s.quantile([0.25, 0.75])
    
    ## 사분위수 범위
    iqr = q3 - q1
    
    ## 하한값 /상한값
    lo , hi = q1-k*iqr, q3 + k*iqr
    
    ## 칯환 후 반환
    return s.clip(lower=lo, upper=hi)


