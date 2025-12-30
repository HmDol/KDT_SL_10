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
##   * 주요 매개변수
##     row, column         : 해당 셀로 위젯을 이동
##     rowspan, columnspan : 현재 배치된 셀에서 지정된 개수만큼 셀 합치기
##     sticky              : 현재 배치된 셀 안에서 위젯 정렬 방법 설정
##        n (north): 위젯을 셀의 상단에 붙임
##        e (east) : 위젯을 셀의 오른쪽에 붙임
##        s (south): 위젯을 셀의 하단에 붙임
##        w (west) : 위젯을 셀의 왼쪽에 붙임 
##        nw (north-west): 위젯을 셀의 왼쪽 상단에 붙임
##        ne (north-east): 위젯을 셀의 오른쪽 상단에 붙임
##        sw (south-west): 위젯을 셀의 왼쪽 하단에 붙임
##        se (south-east): 위젯을 셀의 오른쪽 하단에 붙임
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
window.title("LAYOUT_PACK")
window.geometry('640x400+100+100')
window.resizable(False, False)



## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - Button 요소
## --------------------------------------------------------------------
b1 = tkinter.Button(window, text='(0,0)')
b2 = tkinter.Button(window, text='(0,1)', width = 20)
b3 = tkinter.Button(window, text='(0,2)')

b4 = tkinter.Button(window, text='(1,0)')
b5 = tkinter.Button(window, text='(1,1)')
b6 = tkinter.Button(window, text='(1,3)')

b70 = tkinter.Button(window, text='(2,0)')
b7 = tkinter.Button(window, text='(2,1)')
b8 = tkinter.Button(window, text='(2,2)')
b9 = tkinter.Button(window, text='(2,4)')

##- 화면에 grid방식으로 객체 배치
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0, rowspan=2)
b5.grid(row=1, column=1, columnspan=3)
b6.grid(row=1, column=3)

b70.grid(row=2, column=0)
b7.grid(row=2, column=1, sticky="w")
b8.grid(row=2, column=2)
b9.grid(row=2, column=99)



## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()