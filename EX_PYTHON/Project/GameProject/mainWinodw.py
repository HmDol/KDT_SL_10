from tkinter import*
import subprocess


ROWS = 4
COLS = 4

window = Tk()
window.title("LAYOUT_PACK")
window.geometry("800x800")
window.resizable(False,False)



mainPage_bg = PhotoImage(file="./Images/maintitle.png")

game_1_img = PhotoImage(file="./Images/Game_1.png")
game_2_img = PhotoImage(file="./Images/Game_2.png")
for r in range(ROWS):
    window.grid_rowconfigure(r+1, weight=1, uniform="row") 
for c in range(COLS):
    window.grid_columnconfigure(c, weight=1, uniform="col")

def GAME_1(event):
    print("경찰과 도둑 실행")
    subprocess.run(["python", "pol_the.py"])  

def GAME_2(event):
    print(event)
    subprocess.run(["python", "diff.py"])  

title = Label(window, image=mainPage_bg ,  font=('', 20, 'bold'),anchor='center',relief='solid')
title.grid(row=0, column=0, columnspan=4, padx=4, pady=4, sticky='nsew')

game_1_LB = Label(window, image=game_1_img ,  font=('', 20, 'bold'),anchor='center',relief='solid')
game_1_LB.grid(row=1, column=0, padx=4, pady=4, sticky='nsew')
game_1 = Button(window,text = '경찰과 도둑',font=('', 20, 'bold'), anchor='center',relief='solid' )
game_1.grid(row=1, column=1, columnspan=3, padx=4, pady=4, sticky='nsew')  

game_2_LB = Label(window, image=game_2_img ,  font=('', 20, 'bold'),anchor='center',relief='solid')
game_2_LB.grid(row=2, column=0, padx=4, pady=4, sticky='nsew')
game_2 = Button(window,text = '틀린그림찾기',font=('', 20, 'bold'), anchor='center',relief='solid' )
game_2.grid(row=2, column=1, columnspan=3, padx=4, pady=4, sticky='nsew')  




game_1 .bind("<Button-1>",GAME_1)
game_2 .bind("<Button-1>",GAME_2)
window.mainloop()