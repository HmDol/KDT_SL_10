#include<stdio.h>

int main(void) {
	//변수 선언 및 초기화
	int value[] = { 10, 20, 30, 40, 50 }; // 데이터 저장 변수 선언 + 초기화
	int* p = value;	// 데이터 주소 저장 변수 선언

	//포인터 변수로 배열 원소 출력
	for (int i = 0; i < 5; i++, *++p) {
		printf("%d ", *p);
	}


	if (0) {
		printf("p : 0x%p, value : 0x%p, value[0] : 0x%p\n\n", p, value, &value[0]);

		for (int i = 0; i < 5; i++)
			//printf("value[%d] : %p, %d\n", i, &value[i], value[i]);
			printf("value[%d] : %p, %d\n", i, &value[i], value[i]);

		// 포인터 변수로 배열 원소 접근 ------------------------------------------
		// *p++ : 연산자 우선순위 *(p++)
		//		  -> 후증가로 먼저 현재 주소로 처리 후 주소 1 증가
		printf("p	: %p *p :%d\n", p, *p);
		printf("*p++: %d  p :%p\n", *p++, p);

		// *++p : 연산자 우선순위 *(++p)
	//		  -> 선증가로 주소 증가 후 그곳의 값 역참조
		printf("p	: %p *p :%d\n", p, *p);
		printf("*++p: %d  p :%p\n", *++p, p);
	}

}