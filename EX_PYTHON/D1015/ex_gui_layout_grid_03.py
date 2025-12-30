## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## Container Layout : Grid
##   * 표(행과 열)로 나누어 UI요소 배치
##   * 같은 열에 크기가 다르다면, 가장 큰 길이 기준
##   * 셀 단위로 배치되며, 한 번에 여러 셀 건너 뛰어 배치할 수 없음
##   * pack()과 같이 사용될 수 없음. place()와는 같이 사용할 수 있음
##   * 사용법
##     위젯이름.grid(매개변수1, 매개변수2, 매개변수3, ...)
##   * 분할 비율
## 
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성 및 설정
window=tkinter.Tk()
window.title("** Equal Grid **")
window.geometry("400x200")

##- 전역변수
ROWS = 4
COLS = 4

## ------------------------------------------------------
## 함수기능 : 모든 행/열을 동일 비율로 설정
## 함수이름 : make_equal_grid
## 매개변수 : parent
##           rows
##           cols
## 결과반환 : 없음
## ------------------------------------------------------
def make_equal_grid(parent, rows, cols):
    # 모든 행/열을 동일 비율로
    for r in range(rows):
        parent.grid_rowconfigure(r, weight=1, uniform="row")
    for c in range(cols):
        parent.grid_columnconfigure(c, weight=1, uniform="col")


## --------------------------------------------------------------------
##- 윈도우에 배치될 행과 열 설정
## --------------------------------------------------------------------
## 모든 행/열을 동일 비율로
make_equal_grid(window, ROWS, COLS)

## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - Button 요소
## --------------------------------------------------------------------
titleLB = tkinter.Label(window, text="LOGIN", bd=1, relief="solid")
idLB    = tkinter.Label(window, text="ID", bd=1, relief="solid")
pwLB    = tkinter.Label(window, text="PW", bd=1, relief="solid")

idENT   = tkinter.Entry(window)
pwENT   = tkinter.Entry(window, show="*",)

yesBTN  =tkinter.Button(window, text="YES" )
noBTN   =tkinter.Button(window, text="NO")


## 객체 grid로 배치!

titleLB.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=20, pady=5)

idLB.grid(row=1, column=0,  sticky='nsew', padx=(20,10), pady=5)
idENT.grid(row=1, column=1, columnspan=3, sticky='nsew', padx=(10,20), pady=5)

pwLB.grid(row=2, column=0,  sticky='nsew',padx=(20,10), pady=5)
pwENT.grid(row=2, column=1, columnspan=3, sticky='nsew', padx=(10,20), pady=5)

yesBTN.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=(20,10), pady=10)
noBTN.grid(row=3, column=2, columnspan=2, sticky='nsew', padx=(10,20), pady=10)

## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()