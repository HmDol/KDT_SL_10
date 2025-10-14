## 연습 문제 35.5 날짜 클래스 만들기
class Date:
    @staticmethod
    def is_date_valid(str) :
        year, month, day = map(int, str.split("-"))
        return month <= 12 and day <=31

if Date.is_date_valid('2000-10-01') :
    print('올바른 날짜 형식 입니다.')
else:
    print('잘못된 날짜 형식 입니다.')

## 35.6 심사문제 : 시간 클래스 만들기
class Time :
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    @staticmethod
    def is_time_valid(str) :
        hour, min, sec = map(int, str.split(":"))
        return min <= 60 and sec <=60 and hour <= 23
    
 
    @classmethod
    def from_string(cls, str):
        hour, min, sec = map(int, str.split(":"))
        return cls(hour, min, sec)

time_str = input("시간 입력(ex.23:11:11) => ")

if Time.is_time_valid(time_str) :
    t = Time.from_string(time_str)
    print(t.hour, t.min, t.sec)
else :
    print("잘못된 시간 형식입니다.")

## 36.8 연습문제 : 리스트에 기능 추가하기
class AdvancedList(list):
    def replace(self, old, new):
        while old in self :
            self[self.index(old)] = new

x = AdvancedList([1,2,3,1,2,3,1,2,3])
# print(x.__dict__)
x.replace(1,100)
print(x)

## 36.9 심사 문제 : 다중 상속 사용하기

class Animal :
    def eat(self) :
        print("먹다")
    
class Wing :
    def flap(self) :
        print("파닥거리다")

class Bird(Animal, Wing) :
    def fly(self):
        print("날다")
    pass

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))


## 37.2 연습문제 : 사각형의 넓이 구하기
class Rectangle:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

rect = Rectangle(x1=20, y1=20, x2=40, y2=30)
width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)

## 37.3 심사문제 : 두점 사이의 거리 구하기
import math
class Point2D :
    def __init__(self,x=0 ,y=0):
        self.x = x
        self.y = y

length = 0
p = [Point2D(),Point2D(),Point2D(),Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input("좌표 8개 입력 : ").split())
for x in range(3) :
    length += math.sqrt(abs(p[x].x - p[x+1].x)**2 + abs(p[x].y - p[x+1].y)**2)

print(length)

## 37장 덕 타이핑
class Duck :
    def quack(self) : print("꽥~~~!!!")
    def feather(self ) : print("오리는 흰색과 회색 털을 가지고 있습니다.")

class Person :
    def quack(self) : print("사람이 오리 흉내를 냅니다. 꽥~~!!!")
    def feather(self ) : print("사람은 땅에서 깃털을 주워서 보여줍니다.")

def in_the_forest(obj) :
    obj.quack()
    obj.feather()

donald = Duck()
james = Person()
in_the_forest(donald)
in_the_forest(james)