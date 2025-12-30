## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## 동일 간격 grid 설정
## - 프레임/윈도우(그리드의 부모) 에서 제공 메서드
##  * 행과 열 설정
##  * grid_rowconfigure() / gord_colconfigure()
##      -> 매개변수
##          - weight  : 남는 세로/가로 공간 분배 비율 0(기본, 안늘어남), 1,2,...
##          - minsize : 해당 행/열의 최소 높이(px)
##          - uniform : 같은 키를 가진 행들의 높이를 동일하게 문자열 키(예: 'row')
##                      같은 키끼리 동일 높이로 강제
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성 및 설정
window = tkinter.Tk()
window.title("+++ Equal Grid +++")
window.geometry('900x400')
# window.resizable(False, False)

## - 전역 변수
ROWS    = 3
COLS    = 3
COLORS  = ('yellow', 'lightblue', 'pink')


## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들
## --------------------------------------------------------------------
# 세로 3등분
for r in range(ROWS):
    window.grid_rowconfigure(r, weight=1, minsize= 100, uniform='row')
# window.grid_rowconfigure(2, weight=3, uniform='row') ## 가중치 다르게 해보기

for c in range(COLS):
    window.grid_columnconfigure(c, weight=1, minsize= 10, uniform='col')

## 가로 셀만 
# for r in range(ROWS):
#     f = tkinter.Label( window,bg=COLORS[r % len(COLORS)],text=f'Row {r}')
#     f.grid(row=r, column=0, columnspan=COLS, sticky='nsew', padx=2, pady=2)

# 가로 세로 셀 모두( 이중 반복문 )
for r in range(ROWS):
    for c in range(COLS):
        f = tkinter.Label(window,bg=COLORS[r],text=f'cell_{r}_{c}')
        f.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)

## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()