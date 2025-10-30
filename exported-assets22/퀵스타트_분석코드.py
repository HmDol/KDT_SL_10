"""
🚀 전기화물차 배터리 분석 - 5분 퀵스타트

이 스크립트를 복사해서 Jupyter Notebook이나 Python IDE에서 바로 실행하세요!
"""

# ============================================================================
# 1단계: 라이브러리 임포트
# ============================================================================

import pandas as pd
import numpy as np

# 그래프를 보려면 주석 제거
# import matplotlib.pyplot as plt

print("✅ 라이브러리 로드 완료\n")


# ============================================================================
# 2단계: 데이터 로드
# ============================================================================

# CSV 파일 경로 설정 (자신의 파일 경로로 수정)
file_path = '한국교통안전공단_전기화물차 센서데이터_20230807.csv'

try:
    df = pd.read_csv(file_path, encoding='utf-8')
    print(f"✅ 데이터 로드 성공!")
    print(f"   데이터 크기: {df.shape[0]:,} 행 × {df.shape[1]} 열\n")
except FileNotFoundError:
    print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
    exit()


# ============================================================================
# 3단계: 핵심 컬럼 추출 (간단한 버전)
# ============================================================================

# 모든 컬럼 확인
print("📋 사용 가능한 컬럼 (첫 10개):")
for i, col in enumerate(df.columns[:10], 1):
    print(f"   {i}. {col}")
print(f"   ... (총 {len(df.columns)}개)\n")

# 분석에 사용할 핵심 컬럼 추출
try:
    df_work = df[[
        '속도',
        '배터리_관리_시스템_고전압_팩_전류',
        '배터리_관리_시스템_고전압_팩_전압',
        '배터리_관리_시스템_충전량',
        '차량제어기_액셀',
    ]].copy()
    
    # 이름 바꾸기
    df_work.columns = ['속도', '배터리_전류', '배터리_전압', 'SOC', '액셀']
    
    # 숫자로 변환
    for col in df_work.columns:
        df_work[col] = pd.to_numeric(df_work[col], errors='coerce')
    
    # 결측치 제거
    df_work = df_work.dropna()
    
    print(f"✅ 데이터 정제 완료!")
    print(f"   정제 후 행: {len(df_work):,}개\n")
    
except KeyError as e:
    print(f"❌ 컬럼을 찾을 수 없습니다: {e}")
    print(f"\n사용 가능한 컬럼:")
    for col in df.columns:
        print(f"   - {col}")
    exit()


# ============================================================================
# 4단계: 파생 변수 생성
# ============================================================================

# 순간 전력 계산 (W = V × A)
df_work['순간_전력_kW'] = (df_work['배터리_전압'] * df_work['배터리_전류']) / 1000

# 속도 구간 분류
df_work['속도_구간'] = pd.cut(
    df_work['속도'],
    bins=[-1, 5, 15, 25, 35, 50, 100],
    labels=['정차(0-5)', '저속(5-15)', '중저속(15-25)', '중속(25-35)', '중고속(35-50)', '고속(50+)']
)

print("✅ 파생 변수 생성 완료!\n")


# ============================================================================
# 5단계: 분석 및 결과 출력
# ============================================================================

print("="*80)
print("📊 속도 구간별 배터리 소모 분석")
print("="*80)

# 속도 구간별 통계
speed_stats = df_work.groupby('속도_구간').agg({
    '속도': ['count', 'mean'],
    '배터리_전류': 'mean',
    '순간_전력_kW': 'mean'
}).round(2)

print("\n")
print(speed_stats.to_string())

print("\n" + "="*80)
print("⚡ 주요 발견사항")
print("="*80)

# 최적 구간 찾기
optimal_idx = df_work.groupby('속도_구간')['순간_전력_kW'].mean().idxmin()
optimal_power = df_work.groupby('속도_구간')['순간_전력_kW'].mean().min()

print(f"\n✓ 최적 속도 구간: {optimal_idx}")
print(f"  평균 전력 소모: {optimal_power:.2f} kW")

# 최악의 구간
worst_idx = df_work.groupby('속도_구간')['순간_전력_kW'].mean().idxmax()
worst_power = df_work.groupby('속도_구간')['순간_전력_kW'].mean().max()

print(f"\n⚠️ 가장 비효율적인 구간: {worst_idx}")
print(f"  평균 전력 소모: {worst_power:.2f} kW")
print(f"  효율 차이: {(worst_power / optimal_power):.1f}배")

# 회생 제동 분석
regen_count = len(df_work[df_work['배터리_전류'] < -5])
discharge_count = len(df_work[df_work['배터리_전류'] > 5])

print(f"\n🔋 회생 제동")
print(f"  회생 제동 발생: {regen_count}회")
print(f"  평균 회생 전류: {df_work[df_work['배터리_전류'] < -5]['배터리_전류'].mean():.2f} A")

print(f"\n📈 방전 상태")
print(f"  방전 발생: {discharge_count}회")
print(f"  평균 방전 전류: {df_work[df_work['배터리_전류'] > 5]['배터리_전류'].mean():.2f} A")


# ============================================================================
# 6단계: 결과 저장
# ============================================================================

# 전체 데이터 저장
df_work.to_csv('배터리_분석_데이터.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ 분석 데이터 저장: 배터리_분석_데이터.csv")

# 통계 결과 저장
speed_stats.to_csv('속도별_통계.csv', encoding='utf-8-sig')
print(f"✅ 통계 결과 저장: 속도별_통계.csv")

# 권장사항 저장
recommendations = f"""
전기화물차 배터리 효율 최적화 권장사항
{'='*60}

🎯 핵심 권장사항

1. 최적 속도 유지
   → {optimal_idx} 구간에서 가장 효율적
   → 불필요한 고속 주행 피하기

2. 부드러운 가속
   → 급가속 지양
   → 액셀 페달 부드럽게 조작

3. 회생 제동 활용
   → 브레이크 대신 액셀에서 발 떼기
   → 신호 예측하여 미리 감속

4. 정속 주행
   → 불필요한 가감속 최소화
   → 일정한 속도 유지

💡 기대 효과
   • 배터리 효율 15-25% 개선
   • 주행거리 연장
   • 배터리 수명 증대
"""

with open('권장사항.txt', 'w', encoding='utf-8') as f:
    f.write(recommendations)
print(f"✅ 권장사항 저장: 권장사항.txt")

print("\n" + "="*80)
print("🎉 분석 완료!")
print("="*80)
