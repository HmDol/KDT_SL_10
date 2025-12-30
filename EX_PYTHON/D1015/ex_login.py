import tkinter

window = tkinter.Tk()
window.title("LOGIN")
window.geometry('210x150+400+200')
window.resizable(False, False)


l1 = tkinter.Label(window, text="LOGIN")

l2 = tkinter.Label(window, text="ID", width=7)
l3 = tkinter.Label(window, text="PW")

e1 = tkinter.Entry(window, )
e2 = tkinter.Entry(window, )

b1 = tkinter.Button(window, text="로그인")
b2 = tkinter.Button(window, text="회원가입")



l1.grid( row=0, column=0, columnspan=4) 

l2.grid(row=1, column=0, sticky='nesw')
l3.grid(row=2, column=0, sticky='nesw')

e1.grid(row = 1, column=1, columnspan=3, pady=(10,5))
e2.grid(row = 2, column=1, columnspan=3, pady=(5,10))


b1.grid(row=3, column=0, columnspan=2, sticky='nesw', padx = (10,5))
b2.grid(row=3, column=2, columnspan=2, sticky='nesw')

window.mainloop()
