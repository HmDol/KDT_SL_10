import tkinter as tk

# 계산 함수
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# 버튼 클릭 시 입력창에 숫자/연산자 추가
def on_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("계산기")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text='=', width=22, height=2, font=("Arial", 18), command=calculate).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
