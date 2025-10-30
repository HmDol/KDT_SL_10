## ----------------------------------------------------------------------
## Data에 관련된 공통된 함수들(예시: 속성 출력 기능 함수....)
## ----------------------------------------------------------------------

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
    display(obj.head(3))
    obj.info()
    display(obj.describe(include = include))
    

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