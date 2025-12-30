## -----------------------------------------------------------------------------
## 내장 모듈 random 활용
## - random -> 난수 생성하거나 무작위 선택 할 때 사용
## -----------------------------------------------------------------------------
## [실습1] 로또 프로그램을 구현하세요.
##          - 숫자 범위 : 1 ~ 4
##          - 추출 숫자 : 6개 중복 x
##          - randint 사용
## -----------------------------------------------------------------------------
import random

## 방법 1
list = []
check = []
while True :
    if len(list) == 6: break
    num = random.randint(1,45)
    if(num in check) : 
        continue
    else :
        list.append(num)

print(list)

## 방법 2
s = set()
while True :
    if len(s) == 6: break
    s.add(random.randint(1,45))

print(s)


## 방법 3
print(random.sample(range(1,46),6))