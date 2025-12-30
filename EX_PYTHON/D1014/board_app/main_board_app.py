import tkinter as tk
from tkinter import messagebox, simpledialog
from register_window import RegisterWindow
from login_window import LoginWindow
from edit_user_window import EditUserWindow
from post_list_window import PostListWindow
from post_write_window import PostWriteWindow
from post_edit_delete_window import PostEditDeleteWindow


class MainBoardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("게시판 메인")
        self.geometry("350x400")
        self.current_user = None

        tk.Label(self, text="게시판 프로그램", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="회원가입", width=20, command=self.open_register).pack(pady=5)
        tk.Button(self, text="로그인", width=20, command=self.open_login).pack(pady=5)
        tk.Button(self, text="회원 정보 수정", width=20, command=self.open_edit_user).pack(pady=5)
        tk.Button(self, text="게시글 목록", width=20, command=self.open_post_list).pack(pady=5)
        tk.Button(self, text="게시글 작성", width=20, command=self.open_post_write).pack(pady=5)
        tk.Button(self, text="게시글 수정/삭제", width=20, command=self.open_post_edit_delete).pack(pady=5)
        tk.Button(self, text="종료", width=20, command=self.destroy).pack(pady=20)

    def open_register(self):
        win = RegisterWindow(self)
        win.grab_set()

    def open_login(self):
        win = LoginWindow(self)
        win.grab_set()
        self.wait_window(win)
        if hasattr(win, 'logged_in_user') and win.logged_in_user:
            self.current_user = win.logged_in_user['id']
            messagebox.showinfo("로그인", f"{win.logged_in_user['name']}님 로그인되었습니다.")

    def open_edit_user(self):
        if not self.current_user:
            messagebox.showwarning("경고", "로그인 후 이용하세요.")
            return
        win = EditUserWindow(self, self.current_user)
        win.grab_set()

    def open_post_list(self):
        win = PostListWindow(self)
        win.grab_set()

    def open_post_write(self):
        if not self.current_user:
            messagebox.showwarning("경고", "로그인 후 이용하세요.")
            return
        win = PostWriteWindow(self, self.current_user)
        win.grab_set()

    def open_post_edit_delete(self):
        if not self.current_user:
            messagebox.showwarning("경고", "로그인 후 이용하세요.")
            return
        post_id = simpledialog.askinteger("게시글 번호", "수정/삭제할 게시글 번호를 입력하세요:")
        if not post_id:
            return
        win = PostEditDeleteWindow(self, post_id, self.current_user)
        win.grab_set()

if __name__ == "__main__":
    app = MainBoardApp()
    app.mainloop()
