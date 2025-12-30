import pandas as pd

## 함수
def print_DF(df):
    print("\n--------------속성 읽기 -------------------")
    print('인덱스 :',df.index)
    print('컬럼즈 :',df.columns)
    print(f'데이터 :\n{df.values}, {type(df.values)}')
    print(f'형  태 : {df.shape}') ## 1차원으로 원소 수 반환
    print(f'차  원 : {df.ndim}') ## 1차원
    print(f'타  입 : \n{df.dtypes}')
    print(df)
    print("------------------------------------------------")

## 문제1
print("1")
s1 = pd.Series([100,200,300], name='점수')
print("    ",s1.name)
print(s1)

## 문제2
print("\n2")
s2 = pd.Series([100,200,300],index=['철수','영희','아름'],name='점수')
print("       ",s2.name)
print(s2)


## 문제3
print("\n3")
stock = pd.Series(
    [73000, 356000, 367000, 68600, 34150],
    index=["삼성전자", "셀트리온", "카카오", "삼성전자우", "현대바이오"],
    name="종가"
)

print(stock)
print("\n인덱스 속성\n", stock.index)
print("형태 속성:", stock.shape)


## 문제4
print("\n4")
# 엑셀 파일
def read_excel_file():
    return pd.read_excel("data.xlsx")

# CSV 파일
def read_csv_file():
    return pd.read_csv("data.csv")

# JSON 파일
def read_json_file():
    return pd.read_json("data.json")


## 문제5
print("\n5")
## 5-1 list 타입의 저장
data_list = [['김은수',35, '과장'], ['박정민',30,'대리'], ['이하나',28,'대리']]
cols = ['이름','나이','직책']
df1 = pd.DataFrame(data_list, columns=cols)

## 5-2 dict 타입의 저장
data = {
    "이름": ["김은수", "박정민", "이하나"],
    "나이": [35, 30, 28],
    "직책": ["과장", "대리", "대리"]
}
df2 = pd.DataFrame(data)
print("--------------------리스트로 저장--------------------")
print_DF(df1)
print("--------------------딕셔너리로 저장------------------")
print_DF(df2)

## 문제 6-1
print("\n6")
data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = pd.DataFrame(data, columns=columns)


## 문제 6-2
df.index = ["SK", "PO", "TL", "HMM", "IA", "LG"]

## 문제 6-3
print_DF(df)
print()

## 문제 6-4
print(df.index)
print()
## 문제 6-5
print("형태(shape):", df.shape)
print("차원(ndim):", df.ndim)
print()

## 문제 6-6
print(df.columns)
print()

## 문제 6-7
print(df.values)
print