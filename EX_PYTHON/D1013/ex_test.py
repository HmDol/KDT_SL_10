## ----------------------------------------------------------------
## [복습 - 클래스와 객체 활용]
## - 학생, 의사 클래스 정의
## - 객체 연산자 가능하도록 구현 => 연산자는 마음대로
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## 클래스기능 : 한국 학생 데이터 표현
## 클래스이름 : Student
## 속성/특징 
#      - 공통속성(클래스   속성) : 국적
#      - 각자속성(인스턴스 속성) : 학교, 학번, 이름, 생년월일, 
## 기능/역할
#      - 인스턴스 메서드 : 공부한다, 시험친다, 학생정보출력
## 연산자 오버로딩 : 덧셈 => 점수 덧셈 후 반환
## ----------------------------------------------------------------
class Student: 
    # 클래스 속성 (공유 속성)
    NATIONAL = 'KO'

    # 인스턴스 속성 (개별 속성) => 생성자 메서드(Constructor)
    # 클래스 생성 시 자동 실행되는 메서드
    def __init__(self, school, S_id, major, name, age, grade, score):
        self.school = school
        self.S_id = S_id
        self.major = major
        self.name = name
        self.age = age
        self.grade = grade
        self.score = score

    # 인스턴스 메서드
    # 공부하기 
    # - 매개변수 : self(전달x), subject-과목명
    # - 반환결과 : 반환 없음
    def study(self, subject) :
        print(f'{self.naem}이 {subject}과목을 공부한다.')

    # 시험치기 
    # - 매개변수 : self(전달x), subject-과목명
    # - 반환결과 : 반환 없음
    def exam(self, subject) :
        print(f'{self.naem}이 {subject}과목을 공부한다.')
    
    # 학생정보 출력
    # - 매개변수 : self(전달x)
    # - 반환결과 : 반환 없음
    def printStudent(self) :
        print(f'{"*"*20}')
        print(f'학   교 : {self.school}')
        print(f'학   번 : {self.S_id}')
        print(f'이   름 : {self.name}')
        print(f'학   년 : {self.grade}')
        print(f'나   이 : {self.age}')
        print(f'국   적 : {self.NATIONAL}')
        print(f'{"*"*20}')
        
    # 학생 성적의 합    
    ## 연산자 메서드 오버로딩 => 매개변수 타입, 개수 다른 메서드
    def __add__(self, other) :
        return self.score + other.score


## ----------------------------------------------------------------
## 클래스기능 : 내과 의사 데이터 표현
## 클래스이름 : Doctor
## 속성/특징
#       - 공통속성(클래스   속성) : 분야 
#       - 개별속성(인스턴스 속성) : 병원명, 이름, 경력
#       - 비공개속성 : 의사면허번호
## 기능/역할 : 진료한다, 정보출력, 의사면허번호알력주기
#             비공개 속성 접근 메서드 getter/setter => get만 가능하게
## ----------------------------------------------------------------
class Doctor :
    ## 공통속성
    KIND = '내과'

    ## 인스턴스 속성 초기화, 생성자
    def __init__(self, hname, dname, year, id):
        self.hname = hname
        self.dname = dname
        self.year = year
        ## 비공개 속성
        self.__id = id 

    ## 인스턴스 메서드
    # 진료한다
    # - 매개변수 : self(전달x), 
    # - 반환결과 : 없음 
    def care(self) :
        print(f"{self.name}이 진료한다")

    # 의사정보 출력
    # - 매개변수 : self(전달x), 
    # - 반환결과 : 없음     
    def printDoctor(self) :
        print(f'{"*"*20}')
        print(f'이   름 : {self.dname}')
        print(f'경   력 : {self.year}')    
        print(f'분   야 : {self.KIND}')
        print(f'면   허 : {self.__id}')
        print(f'{"*"*20}')


    ## 비공개 속성 접근 getter 메서드
    # 의사면허 번호 반환
    # - 매개변수 : self(전달x), 
    # - 반환결과 : 의사면허번호 반환 
    def get_id(self):
        return self.__id


