## 28.4 심사 문제 : 파일에서 회문인 단어 출력하기
print("28.4 심사 문제 : 파일에서 회문인 단어 출력하기")
FILE_NAME = './word.txt'

# 파일 생성 
with open(FILE_NAME, mode = 'w', encoding= 'utf-8') as F : 
    s = '''apache
decal
did
neep
noon
refer
river'''
    F.write(s)

## 회문 찾기
with open(FILE_NAME, mode='r', encoding='utf-8') as F:
    while True:
        s = F.readline().strip()
        if not s:
            break
        s1 = list(s)
        s2 = list(s)
        s2.reverse() 

        if s1 == s2:
            print(s)


## 34.6 심사문제 : 게임캐릭터 클래스 만들기
print("34.6 심사문제 : 게임캐릭터 클래스 만들기")
l = input("체력, 마나, AP 입력 (EX. 511.68 334.0 298) : ").split()
hp, mp, ap = map(float, l)
class Annie:
    def __init__(self, hp, mp, ap):
        self.hp = hp
        self.mp = mp
        self.ap = ap

    def tibber(self) :
        print(f'티버 : 피해량 {self.ap * 0.65 + 400}')
        return 

x = Annie(hp, mp, ap)
x.tibber()