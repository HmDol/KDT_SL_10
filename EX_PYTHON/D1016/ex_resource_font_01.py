## =====================================================================
##          Tkinter font
## =====================================================================
## - 한글 폰트명도 인식 가능, OS가 한글 이름 지원하지 않으면 영어식 이름
##
## - 사용법
##   from tkinter import font 
##   font.Font(family="맑은 고딕", size=14, weight="bold", underline=1)
##
## - 속성 
##   * family	    폰트 이름
##   * size	        폰트 크기       (pt 단위)
##   * weight	    굵기            "normal" / "bold"
##   * slant	    기울임          "roman" / "italic"	
##   * underline	밑줄 여부        0 / 1	
##   * overstrike	취소선 여부      0 / 1	
## =====================================================================
## ---------------------------------------------------------------------
## 모듈로딩
## ---------------------------------------------------------------------
import tkinter as tk
from tkinter import font 


## ---------------------------------------------------------------------
## Window 인스턴스 생성 및 폰트 정보 추출 
## ---------------------------------------------------------------------
##- Main Window 인스턴스 생성 및 설정
root = tk.Tk()
root.title("Tkinter 폰트")
root.geometry("800x300+300+300")

##- 폰트 정보 조회 및 출력
fonts = sorted(font.families())
for font in fonts:
    print(f'{font}')

## ---------------------------------------------------------------------
## UI 인스턴스 생성 및 설정
## ---------------------------------------------------------------------
##- Listbox 인스턴스 생성 및 설정
fontLBX = tk.Listbox(root, height=20, width=30)
fontLBX.pack(side='left', fill='y', padx=10, pady=10)
for font in fonts: fontLBX.insert(tk.END, font)

##- Label 인스턴스 생성 및 설정
previewLB = tk.Label(root, text="선택 폰트 미리보기", font=("Arial", 12))
previewLB.pack(side='left')

def show_font(event):
    seletFont = fontLBX.get(fontLBX.curselection())    ## get(선택된 항목의 인덱스 반환 ) -> 해당 인덱스의 값을 반환
    previewLB.config(font=(seletFont, 16))
    previewLB.config(text=f"Sample - {seletFont}")

## ---------------------------------------------------------------------
## UI 인스턴스 이벤트 설정
## ---------------------------------------------------------------------
fontLBX.bind("<<ListboxSelect>>", show_font)


## ---------------------------------------------------------------------
## Window 이벤트 루프
## ---------------------------------------------------------------------
root.mainloop()
