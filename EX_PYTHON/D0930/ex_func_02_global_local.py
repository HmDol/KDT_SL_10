year = 2025 ## 전역변수
print(f'전역변수 year : {year}')
loc = '대구'
def showInfo():
    year = 2030 ## 지역 변수
    print(f'지역변수 year : {year}')
    print(f'우리 지역 : {loc}') ## 지역변수 loc 없음 -> 전역변수 loc 사용

## 전역변수 year 변경
def changeInfo():
    global year    ## 전역함수임을 지정
    year = year +1 ## 전역변수 year 사용
    print(f'전역변수 변경 year : {year}')


showInfo()
changeInfo()
print(f'변경된 year : {year}')


