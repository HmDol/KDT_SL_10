## ----------------------------------------------------------------------------------
## 재귀함수(Recursive Function)
## - 함수 내에서 자기자신을 호출하는 함수
## - 알고리즘 구현에 많이 사용됨
## - 대표 예시 : 피보나치 수열, 펙토리얼
## ----------------------------------------------------------------------------------

## 함수기능 : 팩토리얼
## 함수이름 : nomalFactorial
## 매개변수 : num   - int 정수
## 결과반환 : 팩토리얼 결과 반환
print(list(range(3, 0, -1))) ## 다운 카운팅
def nomalFactorial(num) :
    res = 1
    for x in range(num,0,-1):
        res *= x
    print(res)

nomalFactorial(6)

## 함수기능 : 팩토리얼
## 함수이름 : recFactorial
## 매개변수 : num
## 결과반환 : 팩토리얼 결과 반환
def recFactorial(num) :
    if num == 1:
        return 1
    return num * recFactorial(num-1)

print(recFactorial(6))