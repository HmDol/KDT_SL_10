## --------------------------------------------------------------------------
## 객체지향언어(OOP) 특성 - 다형성
## - 함수/메서드 오버로딩(Overloading)
## - 함수 이름은 동일하지만 매개변수/파라미터 개수, 타입이 다르면 다른 함수로 인식
## --------------------------------------------------------------------------

## --------------------------------------------------------------------------
## - 클래스 정의 : 한국사람
## - 클래스 이름 : KoreanPeople
## - 속      성 :  인스턴스 속성 => 나이, 이름, 성별, __주민번호
##                클래스   속성 => 국적
## - 메  서  드 : 정보 출력 => 인스턴스 메서드
##               비공개 나이계산 기능 => 인스턴스 메서드
## --------------------------------------------------------------------------

class KoreanPeople :
    ## 클래스 속성/변수
    NATIONAL = 'KO'

    ## 인스턴스 생성 및 속성 초기화 메서드
    def __init__ (self, name_, age_, gender_, jumin_):
        self.name = name_
        self.age = age_
        self.gender = gender_
        self.__jumin = jumin_ ## 외부 접근 불가!
        pass

    ## 인스턴스 메서드
    def _print_info(self):
        print("*"*30)
        print(f'이    름 : {self.name}')
        print(f'성    별 : {self.gender}')
        print(f'주민번호 : {self.__jumin}')
        print(f'국    적 : {self.NATIONAL}')
        print("*"*30)

        ## 인스턴스 메서드
    def print_info(self):
        print("*"*30)
        print(f'이    름 : {self.name}')
        print(f'성    별 : {self.gender}')
        print(f'주민번호 : {self.__jumin}')
        print(f'국    적 : {self.NATIONAL}')
        print("*"*30)

    ## 연산자 메서드 오버로딩 => 매개변수 타입, 개수 다른 메서드
    def __add__(self, other) :
        print("__add__()")
        return self.age + other.age

## 객체 인스턴스 생성
hong = KoreanPeople('홍길동', 20, '남자', '051020-3000000')
ma   = KoreanPeople('마징가',  5, '남자', '201103-3111111')

num1 = list([11,22,33])
num2 = list([5,7,9])
print("list 객체 덧셈 :", num1 + num2) ## 리스트 객체끼리 덧셈, 합쳐짐

## KoreanPeople 객체/인스턴스 역산 수행
## => 각 객체의 나이 덧셈 후 반환
print('객체/인스턴스 덧셈 :', hong + ma) ## TypeError -> 연산자 오버로딩 추가 필요!

