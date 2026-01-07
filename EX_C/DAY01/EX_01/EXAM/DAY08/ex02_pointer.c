#include<stdio.h>

int main(void) {
	//변수 선언 및 초기화
	int value = 127;
	int* p = &value;

	printf("변수 읽기 &value: %p, value : %d\n", &value, value);
	printf("변수 읽기 p\t: %p, *p\t: %d\n", p, *p);

	// 포인트변수 기반 값 변경
	*p = *p + 1;

	printf("\n");
	printf("변수 읽기 &value: %p, value : %d\n", &value, value);
	printf("변수 읽기 p\t: %p, *p\t: %d\n", p, *p);


	return 0;
}