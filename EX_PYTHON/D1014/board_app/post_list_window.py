import tkinter as tk
from tkinter import messagebox
import post_data


class PostListWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("게시글 목록")
        self.geometry("500x400")
        self.resizable(False, False)
        self.posts = post_data.load_posts()
        self.listbox = tk.Listbox(self, width=60, height=15)
        self.listbox.pack(pady=10)
        for post in self.posts:
            self.listbox.insert(tk.END, f"[{post['id']}] {post['title']} - {post['author']} ({post['created_at']})")
        self.listbox.bind('<Double-1>', self.show_detail)

    def show_detail(self, event):
        idx = self.listbox.curselection()
        if not idx:
            return
        post = self.posts[idx[0]]
        detail = f"제목: {post['title']}\n작성자: {post['author']}\n작성일: {post['created_at']}\n\n{post['content']}"
        messagebox.showinfo("게시글 상세", detail)

if __name__ == "__main__":
    root = tk.Tk()
    win = PostListWindow(root)
    root.mainloop()
