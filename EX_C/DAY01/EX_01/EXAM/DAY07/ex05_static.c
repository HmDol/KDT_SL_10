#include<stdio.h>

void func1(void) {
	static int sv2 = 1; //생성된 후 1회 초기화, 메모리 유지, 해당 함수에서만 사용가능
	int lv = 1;
	printf("[func1] sv2=%d, lv=%d\n", sv2++, lv++);
}

void func2(void) {
	int sv = 100;
	printf("[func2] sv = %d\n", sv);
	//printf("[func2] static 지역변수 sv2=%d\n", sv2);
}

int main(void) {
	func1();
	func1();
	func1();
	func2();
	
}