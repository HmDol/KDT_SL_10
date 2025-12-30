import tkinter as tk
from tkinter import messagebox
import user_data


class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("로그인")
        self.geometry("300x200")
        self.resizable(False, False)
        tk.Label(self, text="아이디").pack(pady=5)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=5)
        tk.Label(self, text="비밀번호").pack(pady=5)
        self.entry_pw = tk.Entry(self, show="*")
        self.entry_pw.pack(pady=5)
        tk.Button(self, text="로그인", command=self.login).pack(pady=15)
        self.logged_in_user = None

    def login(self):
        user_id = self.entry_id.get().strip()
        pw = self.entry_pw.get().strip()
        users = user_data.load_users()
        user = next((u for u in users if u['id'] == user_id and u['pw'] == pw), None)
        if user:
            self.logged_in_user = user
            messagebox.showinfo("성공", f"{user['name']}님 환영합니다!")
            self.destroy()
        else:
            messagebox.showerror("실패", "아이디 또는 비밀번호가 올바르지 않습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    win = LoginWindow(root)
    root.mainloop()
    if win.logged_in_user:
        print("로그인 성공:", win.logged_in_user)
    else:
        print("로그인 실패 또는 창 닫힘")
