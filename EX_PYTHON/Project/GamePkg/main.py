import tkinter
from PIL import Image, ImageTk

## 게임시작 Click 했을 때
from diff_level_choice import DiffLevelChoice

## 정답 Click 했을 때
from select_correct import selectCorrect

'''
Window
  title     = 틀린그림찾기 메인화면
  size      = 배경 이미지 크기와 동일하게 설정 
  bg        = 이미지로 설정하기
  mainloop  = 반복 실행
  
Button
  1. 게임시작 버튼 => Click, 총 3개의 Level을 선택할 수 있는 창 띄우기
  2. 정    답 버튼 => Click, 각 Level의 정답을 확인할 수 있는 창 띄우기
'''

# ------------------------------------------------------------
# 메인 메뉴 윈도우
# ------------------------------------------------------------
window1 = tkinter.Tk()                  
window1.title("틀린그림찾기 메인화면")
window1.geometry('650x375')              ## 원본 이미지의 1/3크기
window1.resizable(False, False)

# ------------------------------------------------------------
# 배경 이미지 설정
# ------------------------------------------------------------
bg_img = Image.open('../Images/main_bg.png').resize((650, 375))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = tkinter.Label(window1, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------------------------------------------------
# 버튼 스타일
# ------------------------------------------------------------
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_FONT = ("Malgun Gothic", 16, "bold")     ## 맑은 고딕 / 폰트 = 16 / 볼드체
BUTTON_FG = 'white'                             ## 글자 색깔 (전경색)
BUTTON_BG = "#3ec9ff"                         ## 배경색을 하늘 색과 똑같은 색으로 설정

# ------------------------------------------------------------
# 버튼 클릭 시 난이도 선택 창 열기
# ------------------------------------------------------------
def open_diff_choice():
    diff_window = DiffLevelChoice(window1)      ## 부모창(tk.Tk()로 생성한 window) 전달
    diff_window.grab_set()                      ## 모달 효과 (메인창 잠금) -> 현재 화면 위에 팝업처럼 임시로 나타나는 창을 의미

def open_correct() :
    correct_window = selectCorrect(window1)
    correct_window.grab_set()

# ------------------------------------------------------------
# 버튼 구성
# ------------------------------------------------------------
start_button = tkinter.Button(
    window1,
    text='게임시작',
    font=BUTTON_FONT,
    fg=BUTTON_FG,
    bg=BUTTON_BG,
    borderwidth=0,                      ## 버튼 테두리 두께 설정 => 0으로 해서 마치 Label처럼 보이게 설정             
    activebackground=BUTTON_BG,         ## 커서로 누를 때 배경 색상 => 배경색과 동일하게 설정해서 배경 안변하는 것처럼 보이게 함
    activeforeground='#AAAAAA',       ## 커서로 누를 때 글자 색상
    command=open_diff_choice            ## 클릭 관련된 이벤트를 처리할 수 있음 -> 버튼에서 사용하면 용이함  [새로운 창 생성]
)
start_button.place(relx=0.25, rely=0.2, anchor="w", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

howto_button = tkinter.Button(
    window1,
    text='정   답',
    font=BUTTON_FONT,
    fg=BUTTON_FG,
    bg=BUTTON_BG,
    borderwidth=0,
    activebackground=BUTTON_BG,
    activeforeground='#AAAAAA',
    command=open_correct
)
howto_button.place(relx=0.55, rely=0.2, anchor="w", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# ------------------------------------------------------------
# 실행
# ------------------------------------------------------------
window1.mainloop()
