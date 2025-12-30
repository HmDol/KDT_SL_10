## ------------------------------------------------------------------------
## 파일 입출력 - [1]. 파일 읽기
## ------------------------------------------------------------------------
## - 내장함수 : open()
##   * filepath+filename : 존재하면 파일 열기, 없으면 ERROR
##   * mode              : 파일 작업 모드 설정
##                         'r' - 읽기 모드
##   * encoding          : 기계어 변환(코드화)위한 기준 테이블
## ------------------------------------------------------------------------

## 전역변수 정의
FILE_NAME = './test.txt'

## ------------------------------------------------------------------------
## 파일에 읽기 기능
## ------------------------------------------------------------------------
## [1] 파일 열기
textF = open(FILE_NAME, mode='r')
print(type(textF))

## [2] 파일 내용 읽기
## - line 단위 읽기

while True :
    ldata = textF.readline()
    if len(ldata) == 0:
        print("file end")
        break
    print(f'ldata : {ldata.strip()}')   
    print(f'ldata 문자 수 : {len(ldata)}개') 

print("\nempty string")
ldata = textF.readline()
print(f'ldata : {ldata}')
print(f'ldata 문자 수 : {len(ldata)}개')

## [3] 파일 닫기
textF.close()