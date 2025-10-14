import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import post_data


class PostWriteWindow(tk.Toplevel):
    def __init__(self, parent, author):
        super().__init__(parent)
        self.title("게시글 작성")
        self.geometry("400x350")
        self.resizable(False, False)
        self.author = author
        tk.Label(self, text="제목").pack(pady=5)
        self.entry_title = tk.Entry(self, width=40)
        self.entry_title.pack(pady=5)
        tk.Label(self, text="내용").pack(pady=5)
        self.text_content = tk.Text(self, width=40, height=10)
        self.text_content.pack(pady=5)
        tk.Button(self, text="작성", command=self.write_post).pack(pady=15)

    def write_post(self):
        title = self.entry_title.get().strip()
        content = self.text_content.get("1.0", tk.END).strip()
        if not title or not content:
            messagebox.showwarning("입력 오류", "제목과 내용을 모두 입력하세요.")
            return
        posts = post_data.load_posts()
        new_post = {
            "id": len(posts) + 1,
            "author": self.author,
            "title": title,
            "content": content,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        posts.append(new_post)
        post_data.save_posts(posts)
        messagebox.showinfo("성공", "게시글이 작성되었습니다.")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    win = PostWriteWindow(root, 'test')
    root.mainloop()
