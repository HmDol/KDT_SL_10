/***************************************************
* Filename	  : ex01_func.c
* Description : 사용자 정의 함수
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

// user fucntion declaration : 컴파일러에게 알려주는 설명
void printCalc(int a, int b);
int add(int a, int b);
int sub(int a, int b);
void multi(int a, int b);

void main() {
	int a, b;
	printf("a, b 입력(예 3 4) : ");
	scanf("%d %d", &a, &b);

	printCalc(a, b);

}

// 사용자 정의 함수
void printCalc(int a, int b) {
	printf("a + b = %d\n", a + b);
	printf("a - b = %d\n", a - b);
	printf("a * b = %d\n", a * b);
	if (b == 0) printf("유효하지 않음");
	else printf("a / b = %d\n", a / b);


}

int add(int a, int b) {return a + b;}
int sub(int a, int b) { return a - b;}
void multi(int a, int b) { printf("a * b = %d", a * b);}
