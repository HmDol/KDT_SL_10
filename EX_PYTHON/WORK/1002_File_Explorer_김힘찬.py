## ----------------------------------------------
## [실습]
## ----------------------------------------------
## 프로그램 : File_Explorer
## 주요기능 : Windows의 탐색기 기능
##   - 특정 폴더 아래 : 파일, 폴더 목록 출력
##   - 특정 폴더/파일 선택 : 크기, 생성일자 
##   - 상위 폴더 이동 : 상위 폴더의 목록 출력
##   - 첫화면 : 바탕화면
## ----------------------------------------------
import os 
import datetime
os.chdir(r"C:\Users\kdt008\Desktop")

## 현재 위치 파일/디렉 출력
def printList() : 
    print("-------------------------------")
    files = os.listdir()
    for file in files :
        print(file)
    print("상위 폴더 : -1")
    print("종료 : 종료")
    print("-------------------------------")

## 파일 상세 내용 출력
def printDetail(cmd) : 

    print("\n------------상세정보----------------------")
    size = os.path.getsize(cmd)
    ctime = os.path.getctime(cmd)
    cdatetime = datetime.datetime.fromtimestamp(ctime)
    print(f'  -파일명 : {cmd}')
    print(f'  - 크기 : {size} bytes')
    print(f'  - 생성일자 : {cdatetime}')
    print("------------------------------------------")

while True :
    try :
        print("\n\n")
        print("-------------------------------")
        print(f'**현재 위치 : {os.getcwd()}')
        printList()
    
        cmd = input("선택 : ")
        if(cmd == "종료") : break

        if cmd == "-1" : 
            ## 상위폴더로 이동
            os.chdir("..")
        else:
            ## 파일/디렉 판단
            if os.path.exists(cmd) :
                if os.path.isdir(cmd) : 
                    ## 디렉이면 이동
                    os.chdir(cmd)
                else :
                    ## 파일이면 상세정보 출력
                    printDetail(cmd)
                    
            else :
                print("**존재하지 않는 파일/폴더 입니다.**")
    except Exception as e:
        print("**오류발생:",e)
        os.chdir("..")
