## p404 : 31.4
print("31.4")
def is_palindorme(word):
    if len(word) < 2:
        return True 
    if word[0] != word[-1]:
        return False            
    return is_palindorme(word[1:-1]) ## 양쪽을 자르면서 재귀호출
word = input("문자 입력:")
print(is_palindorme(word))

## p404 : 31.5
print("\n31.5")
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2) 
n = input("숫자 입력 : ")
print(fib(int(n)))

## p428. 33.5
print("\n33.5")
def counter():
    i = 0
    def count():
        nonlocal i ## 밖의 i를 사용
        i += 1
        return i
    return count

num = int(input("숫자입력 : "))
c = counter()
for i in range(num):
    print(c(), end=' ')
print()

## p429 : 33.6
print("\n33.6")
def countdown(n):
    def count():
        global n
        n -= 1
        return n + 1
    return count    

n = int(input("숫자 입력 : "))
c = countdown(n)
for i in range(n):
    print(c(), end=' ') 
    