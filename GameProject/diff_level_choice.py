import tkinter as tk
from PIL import Image, ImageTk

# 🔹 하나의 통합 게임 페이지 import
from play_page import FindDifferenceGame  


class DiffLevelChoice(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("난이도 선택")
        self.geometry("650x375")
        self.resizable(False, False)
        self.parent = parent

        # --------------------------------------------------------
        # 배경 이미지
        # --------------------------------------------------------
        bg_img = Image.open('./Images/start_image.jpg').resize((650, 375))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        tk.Label(self, image=self.bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

        # --------------------------------------------------------
        # 제목
        # --------------------------------------------------------
        tk.Label(
            self,
            text="난이도 선택",
            font=("Malgun Gothic", 28, "bold"),
            fg="white",
            bg="#4CAF50"
        ).place(relx=0.5, rely=0.15, anchor="center")

        # --------------------------------------------------------
        # 버튼 생성
        # --------------------------------------------------------
        self.create_level_button("Level 1", 0.40, "Easy")
        self.create_level_button("Level 2", 0.55, "Medium")
        self.create_level_button("Level 3", 0.70, "Hard")

        # --------------------------------------------------------
        # 메뉴로 돌아가기
        # --------------------------------------------------------
        tk.Button(
            self,
            text="메뉴로 돌아가기",
            font=("Malgun Gothic", 12, "bold"),
            bg="#007bff",
            fg="white",
            width=18,
            height=1,
            command=self.destroy
        ).place(relx=0.5, rely=0.88, anchor="center")

    # --------------------------------------------------------
    # 버튼 생성 함수
    # --------------------------------------------------------
    def create_level_button(self, text, rel_y, level):
        def on_click():
            print(f"{level} 난이도로 게임 시작!")
            level_map = {"Easy": 1, "Medium": 2, "Hard": 3}
            game = FindDifferenceGame(self, level=level_map[level])
            game.focus_force()

        tk.Button(
            self,
            text=text,
            font=("Malgun Gothic", 18, "bold"),
            fg="white",
            bg="#3ec9ff",
            width=15,
            height=1,
            relief="raised",
            command=on_click
        ).place(relx=0.5, rely=rel_y, anchor="center")


# ============================================================
# 단독 실행 테스트용
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    choice = DiffLevelChoice(root)
    choice.mainloop()
