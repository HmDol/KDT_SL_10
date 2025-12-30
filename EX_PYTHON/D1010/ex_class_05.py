## --------------------------------------------------------------------------
## 객체지향언어(OOP) 특성 - 정보은닉/캡슐화
## - 파이썬은 모든 속성/메서드 공개를 원칙
## - 비공개 속성 설정 방법 : __속성명
## - 비공개 속성 사용관련 메서드(간접 접근) : getter/setter 메서드 
##      * get속성명()         : 비공개 속성값 읽기
##      * set속성명(새로운 값) : 비공개 속성값 변경 
## --------------------------------------------------------------------------

## --------------------------------------------------------------------------
## - 클래스 정의 : 한국사람
## - 클래스 이름 : KoreanPeople
## - 속      성 :  인스턴스 속성 => 나이, 이름, 성별, __주민번호
##                클래스   속성 => 국적
## - 메  서  드 : 정보 출력 => 인스턴스 메서드
##               비공개 나이계산 기능 => __인스턴스 메서드
##               비공개 속성 간접 접근 => 읽기 메서드 get_jumin()
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
    
    ## 비공개 속성 간접 접근 메서드 => 읽기 메서드
    def get_jumin(self) :
        return self.__jumin

    ## 비공개 속성 간접 변경 메서드 => 변경 메서드
    def set_jumin(self, jumin_) :
        self.__jumin = jumin_

## 객체 인스턴스 생성
hong = KoreanPeople('홍길동', 20, '남자', '051020-3000000')


## --------------------------------------------------------------------------
## 객체 인스턴스의 속성 읽기
print(hong.age)
# print(hong.__jumin) ## ERROR, 비공개 속성 직접 접근!

print(hong.get_jumin()) ## 성공, 비공개 속성 간접 접근!


## --------------------------------------------------------------------------
## 객체/인스턴스 속성 변경
# hong.__jumin = '111' ## 이건 걍 새로 생겨버림
jumin = hong.get_jumin()
jumin = jumin.replace('051020', '050101')
hong.set_jumin(jumin)
print(hong.get_jumin())