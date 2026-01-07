#include<stdio.h>

int main(void) {
	//변수 선언 및 초기화
	int value = 127;
	char ch = 'A';

	int* p;
	p = &value;

	int* p2 = &value;
	char* p3 = &ch;

	// 변수 및 값 확인
	printf("변수 읽기 value\t: %d\n", value);

	printf("변수 읽기 p\t: %p\n", p);
	printf("value 주소 읽기 : %p\n", &value);
	printf("p2 주소 읽기\t: %p\n", p2);


	printf("포인터 변수로 데이터 읽기 *p : %d\n", *p);
	printf("포인터 변수로 데이터 읽기 *p2 : %d\n", *p2);


	//변수들의 데이터 크기 확인 : sizeof()연산자
	printf("\n\n");
	printf("변수 value의 크기 : %zu byte\n", sizeof(value));
	printf("변수		ch의 크기 : %zu byte\n", sizeof(ch));
	printf("변수		 p의 크기 : %zu byte\n", sizeof(p));
	printf("변수		p2의 크기 : %zu byte\n", sizeof(p2));
	printf("변수		p3의 크기 : %zu byte\n", sizeof(p3));

	return 0;
}