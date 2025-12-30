## 1. homework.txt, message.txt 파일을 읽어서 출력하기 코드

with open('./homework.txt', mode='r', encoding='utf-8') as t1 :
    data = t1.read()
    print(data)

with open('./message.txt', mode='r', encoding='ANSI') as t2 :
    print(t2.read())

## 2. data.txt를 복사해서 data_copy.txt생성
with open('./data.txt', mode='r', encoding='utf-8') as f1 :
    data = f1.read()

with open('./data_copy.txt', mode='w', encoding='utf-8') as f2 :
    f2.write(data)