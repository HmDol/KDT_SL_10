import tkinter
from PIL import Image, ImageTk
from diff_level_choice import DiffLevelChoice
from select_correct import selectCorrect

def main():
    # ------------------------------------------------------------
    # 메인 메뉴 윈도우
    # ------------------------------------------------------------
    window1 = tkinter.Tk()
    window1.title("틀린그림찾기 메인화면")
    window1.geometry('650x375')
    window1.resizable(False, False)

    # ------------------------------------------------------------
    # 배경 이미지 설정
    # ------------------------------------------------------------
    bg_img = Image.open('./Images/main_bg.png').resize((650, 375))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tkinter.Label(window1, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ------------------------------------------------------------
    # 버튼 스타일
    # ------------------------------------------------------------
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 50
    BUTTON_FONT = ("Malgun Gothic", 16, "bold")
    BUTTON_FG = 'white'
    BUTTON_BG = "#3ec9ff"

    # ------------------------------------------------------------
    # 버튼 클릭 시 난이도 선택 창 열기
    # ------------------------------------------------------------
    def open_diff_choice():
        diff_window = DiffLevelChoice(window1)
        diff_window.grab_set()

    def open_correct():
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
        borderwidth=0,
        highlightthickness=0,
        activebackground=BUTTON_BG,
        activeforeground='#AAAAAA',
        command=open_diff_choice
    )
    start_button.place(relx=0.25, rely=0.2, anchor="w", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    howto_button = tkinter.Button(
        window1,
        text='정   답',
        font=BUTTON_FONT,
        fg=BUTTON_FG,
        bg=BUTTON_BG,
        borderwidth=0,
        highlightthickness=0,
        activebackground=BUTTON_BG,
        activeforeground='#AAAAAA',
        command=open_correct
    )
    howto_button.place(relx=0.55, rely=0.2, anchor="w", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    # ------------------------------------------------------------
    # 실행
    # ------------------------------------------------------------
    window1.mainloop()

# 이 파일이 직접 실행될 때만 main() 실행
if __name__ == "__main__":
    main()
