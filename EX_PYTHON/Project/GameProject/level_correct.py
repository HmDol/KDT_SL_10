import tkinter as tk
from PIL import Image, ImageTk

class AnswerWindow(tk.Toplevel):
    def __init__(self, parent, img_path):
        super().__init__(parent)

        # -----------------------------
        # 기본 설정
        # -----------------------------
        self.title("정답 보기")
        self.geometry("1200x600")
        self.resizable(False, False)

        # -----------------------------
        # 이미지 불러오기
        # -----------------------------
        try:
            img = Image.open(img_path)
            img = img.resize((1200, 600))  # 창 크기에 맞게 조정
            self.photo = ImageTk.PhotoImage(img)
        except Exception as e:
            tk.Label(self, text=f"이미지 불러오기 오류: {e}", fg="red").pack(pady=20)
            return

        # -----------------------------
        # 이미지 라벨 표시
        # -----------------------------
        tk.Label(self, image=self.photo, bd=2, relief="solid").pack(pady=10)

        # -----------------------------
        # 닫기 버튼
        # -----------------------------
        tk.Button(
            self,
            text="닫기",
            font=("맑은 고딕", 14, "bold"),
            bg="#007bff",
            fg="white",
            width=10,
            height=1,
            command=self.destroy
        ).pack(pady=15)
        

# ============================================================
# 단독 실행 테스트용
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # 테스트용 실행
    win = AnswerWindow(root, "./Images/level1_correct.png")
    win.mainloop()
