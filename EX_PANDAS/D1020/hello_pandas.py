## ---------------------------------------------------------------------
## 데이터 분석 페키지 Pandas
## ---------------------------------------------------------------------
## 모듈 로딩
## ---------------------------------------------------------------------
import pandas as pd

## 기본 정보
print(f'{pd.__version__}')

##다양한 종류의 데이터 파일 로딩
DATA_FILES=["../Data/test.csv", '../Data/test.txt','../Data/test.json']

## ---------------------------------------------------------------------
## 함수명 : pandas.read_파일확장자(파일경로)
## ---------------------------------------------------------------------
## csv ==> DataFrame으로 로딩
dataDF = pd.read_csv(DATA_FILES[0])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{dataDF}')


## txt ==> DataFrame으로 로딩
dataDF = pd.read_table(DATA_FILES[1])
dataDF = pd.read_csv(DATA_FILES[0])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{dataDF}')

## json ==> DataFrame으로 로딩
dataDF = pd.read_json(DATA_FILES[2])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{dataDF}')