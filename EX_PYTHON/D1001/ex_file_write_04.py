## ------------------------------------------------------------------------
## 파일 입출력 - [1]. 파일 쓰기
## ------------------------------------------------------------------------
## - 내장함수 : open()
##   * filepath+filename : 존재하면 내용을 지우고 씀, 없으면 생성 [mode='w']
##   * mode              : 파일 작업 모드 설정
##                         'w' - 기존 내용 삭제, 새롭게 쓰기
##                         'a' - 기존 내용에 추가
##   * encoding          : 기계어 변환(코드화)위한 기준 테이블
## ------------------------------------------------------------------------

## 전역변수 정의
FILE_NAME = './send_msg.txt'

## ------------------------------------------------------------------------
## 파일에 쓰기 기능 => with ~ as 구문
## ------------------------------------------------------------------------
## [1] 파일 - mode = 'w' : 기존 내용 삭제 후 쓰기
## - 영어 외의 입력 시 encoding 지정!!
with open(FILE_NAME, mode='w', encoding='utf-8') as textF:
    data = ['Good Luck',"Happy New Year", '2025', "오늘은 좋은날!"]
    data = [d+"\n" for d in data]
    textF.writelines(data)



FILE_NAME = './send_msg2.txt'

## [2] 파일 - mode = 'a' : 기존 내용에 추가하기(append)
## - 영어 외의 입력 시 encoding 지정!!
with open(FILE_NAME, mode='a', encoding='utf-8') as textF:
    data = ['Good Luck',"Happy New Year", '2025', "오늘은 좋은날!"]
    data = [d+"\n" for d in data]
    textF.writelines(data)  
    

FILE_NAME = './send_msg3.txt'

## [2] 파일 - mode = 'x' : 기존 내용에 추가하기(append) *기존에 있는 파일이면 에러*
## - 영어 외의 입력 시 encoding 지정!!
with open(FILE_NAME, mode='x', encoding='utf-8') as textF:
    data = ['Good Luck',"Happy New Year", '2025', "오늘은 좋은날!"]
    data = [d+"\n" for d in data]
    textF.writelines(data)