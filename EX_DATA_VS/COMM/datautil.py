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




