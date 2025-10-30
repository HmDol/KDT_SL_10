# Pandas 배터리 분석 Cheat Sheet

## 🎯 가장 자주 사용하는 코드 모음

### 데이터 로드 및 기본 정보
```python
# CSV 파일 로드
df = pd.read_csv('파일명.csv', encoding='utf-8')

# 기본 정보
df.shape              # (행, 열) 크기
df.head()             # 첫 5행
df.info()             # 컬럼 정보
df.describe()         # 기본 통계
df.isnull().sum()     # 결측치 개수
```

### 데이터 선택 및 필터링
```python
# 컬럼 선택
df['컬럼명']          # 1개 컬럼
df[['col1', 'col2']]  # 여러 컬럼

# 행 필터링
df[df['속도'] > 30]                    # 조건 필터
df[df['배터리_전류'] > 0]              # 방전 상태만
df[(df['속도'] > 20) & (df['속도'] < 40)]  # 복합 조건

# 특정 범위 추출
df.loc[0:10]          # 인덱스 기반
df.iloc[0:10]         # 위치 기반
```

### 데이터 정제
```python
# 컬럼 이름 변경
df.rename(columns={'기존':'새로운'}, inplace=True)

# 숫자 변환
df['컬럼'] = pd.to_numeric(df['컬럼'], errors='coerce')

# 결측치 처리
df.dropna()           # 결측치 제거
df.fillna(0)          # 0으로 채우기

# 중복 제거
df.drop_duplicates()

# 데이터 타입 변환
df['컬럼'].astype(float)
df['컬럼'].astype(str)
```

### 파생 변수 생성
```python
# 새로운 컬럼 추가
df['순간_전력_kW'] = df['전압'] * df['전류'] / 1000

# 조건부 값 할당
df['상태'] = df['전류'].apply(lambda x: '방전' if x > 0 else '회생')

# 범주화
df['속도_구간'] = pd.cut(df['속도'], 
                          bins=[0, 20, 40, 60],
                          labels=['저속', '중속', '고속'])
```

### 그룹화 및 집계
```python
# 그룹별 평균
df.groupby('속도_구간')['배터리_전류'].mean()

# 여러 함수 적용
df.groupby('속도_구간').agg({
    '배터리_전류': ['mean', 'std', 'min', 'max'],
    '순간_전력_kW': 'mean'
})

# 복합 그룹화
df.groupby(['속도_구간', '상태']).size()
```

### 통계 계산
```python
# 기본 통계
df['컬럼'].mean()     # 평균
df['컬럼'].median()   # 중앙값
df['컬럼'].std()      # 표준편차
df['컬럼'].min()      # 최솟값
df['컬럼'].max()      # 최댓값
df['컬럼'].sum()      # 합계
df['컬럼'].count()    # 개수

# 상관관계
df[['col1', 'col2', 'col3']].corr()

# 백분위수
df['컬럼'].quantile([0.25, 0.5, 0.75])
```

### 정렬 및 순위
```python
# 정렬
df.sort_values('컬럼')              # 오름차순
df.sort_values('컬럼', ascending=False)  # 내림차순

# 상위 N개
df.nlargest(10, '컬럼')
df.nsmallest(5, '컬럼')
```

### 데이터 저장
```python
# CSV 저장
df.to_csv('파일명.csv', index=False, encoding='utf-8-sig')

# Excel 저장
df.to_excel('파일명.xlsx', index=False)

# 텍스트로 저장
df.to_string()
```

### 조인 및 병합
```python
# 수평 결합
pd.concat([df1, df2], axis=1)

# 수직 결합
pd.concat([df1, df2], axis=0)

# 병합
pd.merge(df1, df2, on='공통컬럼')
```

---

## 📊 실제 분석 예제

### 1. 속도 구간별 배터리 소모 분석
```python
# 속도 구간 분류
df['속도_구간'] = pd.cut(df['속도'], 
                          bins=[-1, 15, 25, 35, 50],
                          labels=['저속', '중저속', '중속', '중고속'])

# 그룹 통계
speed_stats = df.groupby('속도_구간').agg({
    '배터리_전류': 'mean',
    '순간_전력_kW': ['mean', 'std'],
    '속도': 'count'
}).round(2)

print(speed_stats)
```

### 2. 최적 속도 찾기
```python
# 전력 소모가 가장 적은 속도 구간
optimal = df.groupby('속도_구간')['순간_전력_kW'].mean().idxmin()
print(f"최적 속도 구간: {optimal}")

# 전력 소모 값
optimal_power = df.groupby('속도_구간')['순간_전력_kW'].mean().min()
print(f"최소 전력 소모: {optimal_power:.2f} kW")
```

### 3. 회생 제동 분석
```python
# 회생 제동 데이터 추출 (음수 전류)
regen = df[df['배터리_전류'] < -5]

print(f"회생 발생 횟수: {len(regen)}")
print(f"평균 회생 전류: {regen['배터리_전류'].mean():.2f} A")
print(f"최대 회생: {regen['배터리_전류'].min():.2f} A")
```

### 4. 가속 강도와 배터리 관계
```python
# 방전 상태에서만 분석
discharge = df[df['배터리_전류'] > 5]

# 액셀 강도 분류
discharge['액셀_강도'] = pd.cut(discharge['액셀'],
                               bins=[0, 30, 60, 90, 100],
                               labels=['약', '중', '강', '급'])

# 액셀 강도별 평균 전력
accel_power = discharge.groupby('액셀_강도')['순간_전력_kW'].mean()
print(accel_power)
```

### 5. 시간대별 효율 비교
```python
# 시간대 구분 (실제 타임스탬프가 있으면)
# df['시간'] = pd.to_datetime(df['타임스탬프']).dt.hour

# 주행 상태별 분석
state_analysis = df.groupby('주행_상태').agg({
    '배터리_전류': 'mean',
    '속도': 'mean',
    '순간_전력_kW': 'mean'
}).round(2)

print(state_analysis)
```

### 6. 상관관계 찾기
```python
# 배터리 전류와 다른 변수의 상관관계
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr = df[numeric_cols].corr()

# 배터리 전류와의 상관관계 정렬
print(corr['배터리_전류'].sort_values(ascending=False))
```

---

## 🎨 시각화 예제

### 1. 기본 그래프
```python
import matplotlib.pyplot as plt

# 속도 구간별 전력 소모
speed_power = df.groupby('속도_구간')['순간_전력_kW'].mean()
speed_power.plot(kind='bar')
plt.title('속도 구간별 전력 소모')
plt.ylabel('전력 (kW)')
plt.show()
```

### 2. 산점도
```python
plt.scatter(df['속도'], df['순간_전력_kW'], alpha=0.6)
plt.xlabel('속도 (km/h)')
plt.ylabel('전력 (kW)')
plt.title('속도 vs 전력')
plt.show()
```

### 3. 상관관계 히트맵
```python
import seaborn as sns

corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.show()
```

### 4. 박스 플롯
```python
df.boxplot(column='배터리_전류', by='주행_상태')
plt.title('주행 상태별 배터리 전류')
plt.show()
```

### 5. 여러 그래프 한번에
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1번 그래프
df.groupby('속도_구간')['순간_전력_kW'].mean().plot(ax=axes[0, 0], kind='bar')
axes[0, 0].set_title('속도 구간별 전력')

# 2번 그래프
axes[0, 1].scatter(df['속도'], df['배터리_전류'])
axes[0, 1].set_title('속도 vs 전류')

# ... 등등

plt.tight_layout()
plt.savefig('분석.png', dpi=100)
plt.show()
```

---

## 🐛 일반적인 오류와 해결법

### KeyError: '컬럼명'
```python
# 원인: 컬럼 이름 오타 또는 존재하지 않음
# 해결: 컬럼 목록 확인
print(df.columns)

# 또는 리네이밍
df.rename(columns={'잘못된이름': '올바른이름'}, inplace=True)
```

### TypeError: cannot perform reduce with flexible type
```python
# 원인: 숫자가 아닌 값이 포함됨
# 해결: 타입 변환
df['컬럼'] = pd.to_numeric(df['컬럼'], errors='coerce')
df = df.dropna()
```

### UnicodeDecodeError
```python
# 원인: 인코딩 문제
# 해결: 인코딩 명시
df = pd.read_csv('파일.csv', encoding='utf-8')
# 또는 'euc-kr', 'cp949' 등 시도
```

### SettingWithCopyWarning
```python
# 원인: 복사본이 아닌 뷰에 대해 수정
# 해결: 명시적 복사
df_work = df[df['속도'] > 20].copy()
df_work['새컬럼'] = 값
```

---

## 📚 유용한 팁

### 1. 데이터 미리보기
```python
# 샘플 출력
df.sample(5)

# 특정 범위만 보기
df.iloc[100:110]
```

### 2. 메모리 절약
```python
# 데이터 타입 최적화
df['컬럼'] = df['컬럼'].astype('int32')  # int64 대신

# 필요한 컬럼만 로드
cols_to_use = ['속도', '배터리_전류']
df = pd.read_csv('파일.csv', usecols=cols_to_use)
```

### 3. 빠른 처리
```python
# 대용량 파일은 청크로 읽기
for chunk in pd.read_csv('큰파일.csv', chunksize=10000):
    # 처리
    pass

# 병렬 처리
from pandarallel import pandarallel
pandarallel.initialize()
df['new_col'] = df['col'].parallel_apply(함수)
```

### 4. 고급 필터링
```python
# isin으로 여러 값 필터링
df[df['상태'].isin(['가속', '정속'])]

# str 메서드
df[df['컬럼'].str.contains('검색어')]

# between
df[df['속도'].between(20, 40)]

# query
df.query('속도 > 20 and 배터리_전류 > 0')
```

---

## 🚀 한 줄 분석

```python
# 가장 높은 전력 소모 주행 상태
df.groupby('주행_상태')['순간_전력_kW'].mean().max()

# 회생 제동으로 회수한 에너지
abs(df[df['배터리_전류'] < 0]['순간_전력_kW'].sum())

# 최대 속도일 때의 평균 전력
df[df['속도'] == df['속도'].max()]['순간_전력_kW'].mean()

# 가장 효율적인 운전 상태
df.nsmallest(1, '순간_전력_kW')[['속도', '배터리_전류', '순간_전력_kW']]
```

---

이 Cheat Sheet를 북마크해두고 필요할 때마다 참고하세요! 🎯
