## -----------------------------------------------------------
## Python GUI Programming - Tkinter
## ** Entry Widget : 사용자의 텍스트 요청을 전달받는 입력 ui요소
## -----------------------------------------------------------
## 모듈 로딩
## -----------------------------------------------------------
from tkinter import *

import os                       # 이미지 경로 관련 모듈
from PIL import Image, ImageTk ## TK 미지원 이미지 처리위한 모듈

## --------------------------------------------------------
## 사용자 정의 함수
## --------------------------------------------------------
##=> 지원&미지원 이미지 처리
## - 함수 기능 : 이미지 데이터에서 TKinter용 이미지 추출 후 반환 
## - 함수 이름 : get_img
## - 매개 변수 : imgpath - 이미지명 포함 경로
## - 반환 결과 : tk용 이미지 데이터
## --------------------------------------------------------
def get_img(imgpath):
    _ , ext = os.path.splitext(imgpath)
    if ext in ['.png', '.bmp', '.gif', '.ppm', '.pgm'] :
        return PhotoImage(file = imgpath)
    else :
        ## 순수 이미지 데이터 추출
        img = Image.open(imgpath)
        window_width = 200
        window_height = 200
        img.thumbnail((window_width, window_height))  
        ## 이미지 데이터 전달
        return ImageTk.PhotoImage(img)


## -----------------------------------------------------------
##- 윈도우 관련
## -----------------------------------------------------------
mainWin = Tk()

mainWin.title("나의 첫 GUI 프로그램")
mainWin.geometry("400x800+600+300") # 가로x세로+x좌표+y좌표
# mainWin.resizable(False, False) # 창 크기 조절
# mainWin.option_add("*Font", "궁서체") # 폰트 설정
# mainWin.grid_bbox() # 그리드 박스 설정

## -----------------------------------------------------------
##- 윈도우에 배치될 UI요소들
## -----------------------------------------------------------
## - 텍스트 라벨 객체 생성--------------------------------
l1 = Label(
    text="고양이 월드",
    width=20, height=3,
    fg="blue", bg="yellow",
    font=("궁서체", 20),
    relief="solid"
)

## - 이미지 라벨 생성-------------------------------------
IMG_FILE1 = '../Images/image1.png'
IMG_FILE2 = '../Images/image2.jpg'


# 이미지 객체를 참조로 유지해야 이미지가 정상 표시됨
imgVar = get_img(IMG_FILE2)
img1 = Label(
    mainWin,
    image=imgVar,


)

# imgVar2 = get_img(IMG_FILE1)
# img2 = Label(
#     mainWin,
#     image = imgVar2
# )


## entry 라벨 요소 ------------------------------------------------
## 인스턴스 생성
inputFD = Entry(mainWin,
                text = '메세지를 입력하세요!',
                show="*",
                foreground='green',
                background='grey'
                )








## UI를 윈도우에 배치   -----------------------------------
l1.pack()
img1.pack(pady = 30)
# img2.pack(side='right')
inputFD.pack()

## 윈도우에서 발생하는 사용자 이벤트 수신
## 윈도우 종료될 때 까지 실행
mainWin.mainloop()