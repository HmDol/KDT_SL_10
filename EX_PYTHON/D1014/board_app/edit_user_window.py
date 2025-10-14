import tkinter as tk
from tkinter import messagebox
import user_data


class EditUserWindow(tk.Toplevel):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        self.title("회원 정보 수정")
        self.geometry("300x250")
        self.resizable(False, False)
        self.user_id = user_id
        self.users = user_data.load_users()
        self.user = next((u for u in self.users if u['id'] == user_id), None)
        if not self.user:
            messagebox.showerror("오류", "사용자 정보를 찾을 수 없습니다.")
            self.destroy()
            return
        tk.Label(self, text="아이디").pack(pady=5)
        tk.Label(self, text=self.user['id']).pack(pady=5)
        tk.Label(self, text="비밀번호").pack(pady=5)
        self.entry_pw = tk.Entry(self, show="*")
        self.entry_pw.insert(0, self.user['pw'])
        self.entry_pw.pack(pady=5)
        tk.Label(self, text="이름").pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.insert(0, self.user['name'])
        self.entry_name.pack(pady=5)
        tk.Button(self, text="수정", command=self.edit_user).pack(pady=15)

    def edit_user(self):
        pw = self.entry_pw.get().strip()
        name = self.entry_name.get().strip()
        if not pw or not name:
            messagebox.showwarning("입력 오류", "비밀번호와 이름을 입력하세요.")
            return
        self.user['pw'] = pw
        self.user['name'] = name
        user_data.save_users(self.users)
        messagebox.showinfo("성공", "회원 정보가 수정되었습니다.")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    win = EditUserWindow(root, 'test')
    root.mainloop()
