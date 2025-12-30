## --------------------------------------------------------------------------
## 객체지향언어(OOP) 특성 - 정보은닉/캡슐화
## - 파이썬은 모든 속성/메서드 공개를 원칙
## - 비공개 속성 설정 방법 : __속성명
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
    
    def __calc_age(self, year) :
        self.age = year - self.age + 1


p1 = KoreanPeople('홍길동', 20, '남자', '051020-3000000')
p1.print_info()

## 변경
p1.age = 21
print(p1.age)

## ERROR, 없다고 뜸
# print(p1.__jumin) 

## 변경되는거 같지만, 새로운 속성으로 추가되는 거임;;
p1.__jumin = '111111 - 11111111'

print(p1.__dict__)
p1.print_info()

## 비공개 메서드 사용 ==> 에러
# p1.__calc_age(2026)
print(p1.__dict__)