import tkinter as tk
from tkinter import messagebox
import post_data


class PostEditDeleteWindow(tk.Toplevel):
    def __init__(self, parent, post_id, current_user):
        super().__init__(parent)
        self.title("게시글 수정/삭제")
        self.geometry("400x350")
        self.resizable(False, False)
        self.post_id = post_id
        self.current_user = current_user
        self.posts = post_data.load_posts()
        self.post = next((p for p in self.posts if p['id'] == post_id), None)
        if not self.post:
            messagebox.showerror("오류", "게시글을 찾을 수 없습니다.")
            self.destroy()
            return
        if self.post['author'] != current_user:
            messagebox.showerror("권한 오류", "본인 게시글만 수정/삭제할 수 있습니다.")
            self.destroy()
            return
        tk.Label(self, text="제목").pack(pady=5)
        self.entry_title = tk.Entry(self, width=40)
        self.entry_title.insert(0, self.post['title'])
        self.entry_title.pack(pady=5)
        tk.Label(self, text="내용").pack(pady=5)
        self.text_content = tk.Text(self, width=40, height=10)
        self.text_content.insert("1.0", self.post['content'])
        self.text_content.pack(pady=5)
        tk.Button(self, text="수정", command=self.edit_post).pack(pady=5)
        tk.Button(self, text="삭제", command=self.delete_post).pack(pady=5)

    def edit_post(self):
        title = self.entry_title.get().strip()
        content = self.text_content.get("1.0", tk.END).strip()
        if not title or not content:
            messagebox.showwarning("입력 오류", "제목과 내용을 모두 입력하세요.")
            return
        self.post['title'] = title
        self.post['content'] = content
        post_data.save_posts(self.posts)
        messagebox.showinfo("성공", "게시글이 수정되었습니다.")
        self.destroy()

    def delete_post(self):
        if messagebox.askyesno("삭제 확인", "정말로 삭제하시겠습니까?"):
            self.posts = [p for p in self.posts if p['id'] != self.post_id]
            for idx, p in enumerate(self.posts, 1):
                p['id'] = idx
            post_data.save_posts(self.posts)
            messagebox.showinfo("성공", "게시글이 삭제되었습니다.")
            self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    win = PostEditDeleteWindow(root, 1, 'test')
    root.mainloop()
