import tkinter as tk
from PIL import Image, ImageTk


class FindDifferenceGame(tk.Toplevel):
    def __init__(self, parent, level=1):
        super().__init__(parent)
        self.title(f"틀린그림 찾기 - LEVEL {level}")
        self.geometry("1300x800")
        self.resizable(False, False)

        # -----------------------------
        # 레벨별 데이터 설정
        # -----------------------------
        level_data = {
            1: {
                "IMG1": '../Images/level1_1.png',
                "IMG2": '../Images/level1_2.png',
                "ANS": x,
            },
            2: {
                "IMG1": '../Images/level2_1.png',
                "IMG2": '../Images/level2_2.png',
                "ANS": [[421,82], [532, 366], [219, 94], [147,141]],
            },
            3: {
                "IMG1": '../Images/level3_1.png',
                "IMG2": '../Images/level3_2.png',
                "ANS": [[191,137], [185, 286], [392, 312], [284,414]] ,
            }
        }

        # 선택한 레벨의 데이터 적용
        self.level = level
        data = level_data.get(level)
        self.IMG1 = data["IMG1"]
        self.IMG2 = data["IMG2"]
        self.arr = data["ANS"]

        # -----------------------------
        # 공통 게임 설정
        # -----------------------------
        self.TIME = 1
        self.TARGET = len(self.arr) ## 정답 
        self.CHECK_IMG = '../Images/greenCheck.png'

        # 상태 변수
        self.score = 0
        self.found_points = []
        self.check_marks = []
        self.check_photos = []

        # UI 구성
        self.create_widgets()
        self.create_checkmarks()
        self.update_status_label()
        self.timer()

    # ============================================================
    def create_widgets(self):
        self.xyLB = tk.Label(self, text="", font=("맑은 고딕", 40, "bold"), fg="blue")
        self.xyLB.pack(pady=10)

        self.timeFM = tk.Frame(self, bg='lightyellow', bd=2, relief='solid', width=50, height=600)
        self.timeBAR = tk.Label(self.timeFM, bg='red')
        self.timeFM.pack(side="left", padx=10, pady=10)
        self.timeBAR.place(x=0, y=0, relwidth=1, relheight=0.0)

        img1 = Image.open(self.IMG1).resize((600, 600))
        img2 = Image.open(self.IMG2).resize((600, 600))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_label1 = tk.Label(self, image=self.photo1, bd=2, bg='black')
        self.img_label2 = tk.Label(self, image=self.photo2, bd=2, bg='black')


        self.img_label1.pack(side='left', padx=10)
        self.img_label2.pack(side='left', padx=10)

        self.img_label1.bind("<Button-1>", self.find_click)
        self.img_label2.bind("<Button-1>", self.find_click)

    # ============================================================
    def create_checkmarks(self):
        check_img = Image.open(self.CHECK_IMG).convert("RGBA").resize((40, 40))
        check_photo = ImageTk.PhotoImage(check_img)
        self.check_photos.append(check_photo)

        for _ in range(self.TARGET * 2):
            mark = tk.Label(self, image=check_photo, bg="white", bd=0)
            mark.place_forget()
            self.check_marks.append(mark)

    # ============================================================
    def update_status_label(self):
        self.xyLB.config(text=f"LEVEL {self.level} | 현재 {self.score} / 목표 {self.TARGET}")

    # ============================================================
    def find_click(self, event):
        x, y = event.x, event.y
        print(f'x = {x} , y = {y}')
        for (tx, ty) in self.arr:
            if (tx - 20 <= x <= tx + 20) and (ty - 20 <= y <= ty + 20):
                if (tx, ty) not in self.found_points:
                    self.found_points.append((tx, ty))
                    self.mark_correct(tx, ty)
                    self.score += 1
                    self.update_status_label()
                    if self.score == self.TARGET:
                        self.xyLB.config(text=f"🎉 LEVEL {self.level} CLEAR 🎉", fg="green")
                    break

    # ============================================================
    def mark_correct(self, x, y):
        idx = self.score * 2
        if idx + 1 >= len(self.check_marks): 
            return
        self.check_marks[idx].place(in_=self.img_label1, x=x-20, y=y-20)
        self.check_marks[idx + 1].place(in_=self.img_label2, x=x-20, y=y-20)

    # ============================================================
    def timer(self, n=0.0):
        if n >= self.TIME:
            if self.score < self.TARGET:
                self.xyLB.config(text=f"⏰ LEVEL {self.level} FAILED ❌", fg="red")
                self.after(2000, self.destroy)
            return
        self.timeBAR.place_configure(relheight=n)
        self.after(200, lambda: self.timer(n + 0.01))


# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()

    # 테스트 용
    # FindDifferenceGame(root, level=1).mainloop()
    # FindDifferenceGame(root, level=2).mainloop()
    # FindDifferenceGame(root, level=3).mainloop()
