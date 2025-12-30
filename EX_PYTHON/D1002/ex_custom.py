## ------------------------------------------------------------------==
## 개발자/사용자 정의 모듈 및 패키지 사용하기
## 
## - 모듈 : 파이썬 파일(.py) 1개
## - 패키지 : 모듈 여러개 묶은 것 
## ------------------------------------------------------------------==
## 모듈 로딩
## - D1002
##     |-- ex_custom.py *
##     |-- utils.py
##     |-- func
##          |-- my_func.py
## - COMM
##     |--- display.py
## ------------------------------------------------------------------==
## 같은 위치에 존제하는 모듈
import utils

## 하위 폴더에 존재하는 모듈
import func.my_func as mf

## 상위 폴더에 존재하는 모듈 가져오기
import sys
sys.path.append(r'C:\Users\kdt008\Desktop\KDT_10SL\EX_PYTHON\COMM')
import display

## 모듈 사용
utils.print_msg("Good Luck 2025")
r1, r2, r3, r4 = mf.calc(3,4)
print(f'+ => {r1}')
print(f'- => {r2}')
print(f'* => {r3}')
print(f'/ => {r4}')


display.show()