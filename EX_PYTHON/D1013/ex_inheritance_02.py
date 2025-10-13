## ----------------------------------------------------------------------------
## 상속(Inheritance)
## - 클래스 재사용 및 확장 용도
## - 구성 : 부모/super 클래스 <-- 자식/sub 클래스
## ----------------------------------------------------------------------------
## Point 데이터 표현 클래스
## - 클래스 이름 : Point
## - 속성 / 특징 : 
#       - 클래스 속성 : 없음
#       - 인스턴스 속성 : x, y, color
#       - 비공개 속성 : 없음
## - 기능 / 역할 : 그리기, 정보출력
## ----------------------------------------------------------------------------
class Point :
    ##- 메모리 스캔 및 할당 메서드, 가장 먼저 호출됨 --------------------
    ## cls : 클래스 정보 
    def __new__(cls, *args, **kwargs): 
        print('from new')
        obj = super().__new__(cls)
        return obj
    
    ## 인스턴스 속성 초기화 메서드 -------------------------------------
    ## - self : 인스턴스 정보, 메모리 주소
    def __init__(self, x=0, y=0, color = 'black'):
        print('from init')
        self.x = x
        self.y = y
        self.color = color


    ## 인스턴스 메서드 => self -----------------------------------------

    ## 그리기
    ## 기   능 : 지정된 좌표에 점 그리기
    ## 이   름 : drawing
    ## 매개변수 : self
    ## 반환결과 : 없음
    def drawing(self) :
        print(f'({self.x},{self.y})에 {self.color}점 그리기')

    ## 정보출력
    ## 기   능 : 지정된 좌표에 점 그리기
    ## 이   름 : drawing
    ## 매개변수 : self
    ## 반환결과 : 없음
    def print_info(self) :
        print(f'색상 : {self.color}')         
        print(f'위치 : ({self.x}, {self.y})')


## ----------------------------------------------------------------------------
## Point 3D 데이터 표현 클래스
## - 클래스 이름 : Point3D
## - 부모 클래스 : Point
## - 속성 / 특징 : 
#       - 클래스 속성 : 없음
#       - 인스턴스 속성 : x, y, z, color
#       - 비공개 속성 : 없음
## - 기능 / 역할 : 그리기, 정보출력
## ----------------------------------------------------------------------------

class Point3D(Point) :
    ##- 메모리 스캔 및 할당 메서드, 가장 먼저 호출됨 --------------------
    ## cls : 클래스 정보 
    def __new__(cls, *args, **kwargs): 
        print('from new Pinte3D')
        obj = super().__new__(cls)
        return obj
    
    ## 인스턴스 속성 초기화 메서드 -------------------------------------
    ## - self : 인스턴스 정보, 메모리 주소
    def __init__(self, x=0, y=0, z=0, color = 'black'):
        super().__init__(x, y, color)
        print('from init Point3D')
        self.z = z
    
    #### 오버라이딩 : 상속관계 #####
    ## 기   능 : 지정된 좌표에 점 그리기
    ## 이   름 : drawing
    ## 매개변수 : self
    ## 반환결과 : 없음
    def drawing(self) :
        print(f'({self.x},{self.y}, {self.z})에 {self.color}점 그리기')

## 테스트용 - 동일부모 클래스
class Line(Point):
    pass

## -------------------------------------------------------------------------
## 인스턴스/객체 생성 및 활용
## -------------------------------------------------------------------------
p1 = Point3D(x =10, y=25, color="red")
l1 = Line()

p1.drawing()
p1.print_info()


## -------------------------------------------------------------------------
## 인스턴스/객체 관련 메서드들
## -----------------------------------------------------------------------
## => 부모/자식 관계 검사 issubclass(자식 , 부모)
print("issubclass(Point3D, Point) :" , issubclass(Point3D, Point))

## 인스턴스 검사 isinstance(변수명, 클래스이름)
print("isinstance(p1, Point3D) :", isinstance(p1, Point3D))
print("isinstance(p1, Point) :", isinstance(p1, Point))

print("isinstance(l1, Point3D) :", isinstance(l1, Line))
print("isinstance(l1, Point) :", isinstance(l1, Point))
