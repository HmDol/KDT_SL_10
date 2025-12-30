import tkinter as tk
from tkinter import messagebox
import user_data


class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("회원가입")
        self.geometry("300x250")
        self.resizable(False, False)
        tk.Label(self, text="아이디").pack(pady=5)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=5)
        tk.Label(self, text="비밀번호").pack(pady=5)
        self.entry_pw = tk.Entry(self, show="*")
        self.entry_pw.pack(pady=5)
        tk.Label(self, text="이름").pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)
        tk.Button(self, text="회원가입", command=self.register).pack(pady=15)

    def register(self):
        user_id = self.entry_id.get().strip()
        pw = self.entry_pw.get().strip()
        name = self.entry_name.get().strip()
        
        if not user_id or not pw or not name:
            messagebox.showwarning("입력 오류", "모든 항목을 입력하세요.")
            return
        users = user_data.load_users()
        if any(u['id'] == user_id for u in users):
            messagebox.showerror("중복 오류", "이미 존재하는 아이디입니다.")
            return
        users.append({"id": user_id, "pw": pw, "name": name})
        user_data.save_users(users)
        messagebox.showinfo("성공", "회원가입이 완료되었습니다.")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    win = RegisterWindow(root)
    root.mainloop()
