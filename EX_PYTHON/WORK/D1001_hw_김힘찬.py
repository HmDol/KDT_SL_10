## ----------------------------------------------------------------
## 주소록 만들기
## - 기능 : 추가/삭제/수정/기록
## ----------------------------------------------------------------
F_NAME = './history.txt'

## 메인 메뉴 출력
def printMenu() :
    print(f'{"선택":-^20}')
    print(f'{"1. 추 가":^20}')
    print(f'{"2. 삭 제":^20}')
    print(f'{"3. 수 정":^20}')
    print(f'{"4. 기 록":^20}')
    print(f'{"5. 종 료":^20}')
    print(f'{"":-^22}')

## 주소 추가
def addAddress() :
    name = input("이름 입력 : ")
    address = input("주소 입력 : ")
    print(f'{name} : {address} 추가되었습니다.')
    addHistory(f'{name}:{address}')

## 기록 추가
def addHistory(data, filename=F_NAME):
    with open(filename, mode='a', encoding="utf-8") as F:
        F.write(data+'\n')

## 기록 출력
def printHistory(filename=F_NAME):
    with open(filename, mode='r', encoding='utf-8') as F:
        lines = [line.strip() for line in F.readlines()]

    if(len(lines) == 0) :
        print("기록이 없습니다.")
        return
    
    print(f'{"기록":-^20}')
    for i, line in enumerate(lines, 1):
        print(f'{i}. {line}')
    print(f'{"":-^22}')

## 주소 삭제
def deleteAddress(filename=F_NAME):
    name = input("삭제할 이름 입력 : ")
    
    with open(filename, 'r', encoding='utf-8') as F:
        lines = [line.strip() for line in F.readlines()]
  
    if(len(lines) == 0) :
        print("기록이 없습니다.")
        return

    new_lines = [line for line in lines if not line.startswith(name + ":")]

    if len(new_lines) == len(lines):
        print(f"{name} 이름을 찾을 수 없습니다.")
    else:
        with open(filename, 'w', encoding='utf-8') as F:
            for line in new_lines:
                F.write(line + '\n')
        print(f"{name} 주소가 삭제되었습니다.")

## 주소 수정
def modifyAddress(filename=F_NAME):
    name = input("수정할 이름 입력 : ")
 
    with open(filename, 'r', encoding='utf-8') as F:
        lines = [line.strip() for line in F.readlines()]
    if(len(lines) == 0) :
        print("기록이 없습니다.")
        return
    
    new_lines = [line for line in lines if not line.startswith(name + ":")]
    if len(new_lines) == len(lines):
        print(f"{name} 이름을 찾을 수 없습니다.")
    else :
        new_address = input("새로운 주소 입력 : ")
        new_lines.append(f"{name}:{new_address}")
        with open(filename, 'w', encoding='utf-8') as F:
            for line in new_lines:
                F.write(line + '\n')
        print(f"{name} 주소가 수정되었습니다.")    


## 메인 루프
while True:
    printMenu()
    cmd = input("선택 : ")
    if cmd == '5':
        break
    elif cmd == "1":
        addAddress()
    elif cmd == "2":
        deleteAddress()
    elif cmd == "3":
        modifyAddress()
    elif cmd == "4":
        printHistory()
    else:
        print("잘못 입력하셨습니다.")

print("종료되었습니다.")
