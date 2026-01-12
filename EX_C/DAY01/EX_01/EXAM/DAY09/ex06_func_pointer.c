#include<stdio.h>

// 함수와 포인터

int add(int a, int b) {
	return a + b;

}
int pow(int a, int b){
	return a * b;
}
float div(int a, int b) {
	return a / b;
}
int sub(int x, int y) {
	return x - y;
}
void msg() {
	printf("Good Luck!");
}

int main(void) {
	// 함수 포인터 변수 선언 및 초기화
	int (*pAdd)(int, int) = add;
	int (*pDiv)(int, int) = div;
	void (*pMsg)() = msg;
	int (*pFunc[3]) (int, int) = { add, pow, sub };

	printf("add Func :%p, pAdd: %p\n", add, pAdd); // 같은 주소값을 가지고 있음
	printf("div Func :%p, pDiv: %p\n", div, pDiv);
	
	//함수 실행
	printf("pAdd(10, 20) = %d\n", pAdd(10, 20));
	pMsg();

	return 0;
}