## -----------------------------------------------------------
## Python GUI Programming - Tkinter
## -----------------------------------------------------------
## 모듈 로딩
## -----------------------------------------------------------
from tkinter import *

## - 윈도우 창 생성
mainWin = Tk()

mainWin.title("나의 첫 GUI 프로그램")
mainWin.resizable(False, False) # 창 크기 조절
mainWin.geometry("400x300+600+300") # 가로x세로+x좌표+y좌표

# mainWin.option_add("*Font", "궁서체") # 폰트 설정
# mainWin.grid_bbox() # 그리드 박스 설정

## 윈도우에서 발생하는 사용자 이벤트 수신
## 윈도우 종료될 때 까지 실행
mainWin.mainloop()