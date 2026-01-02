/***************************************************
* Filename	  : ex11_switch_case.c
* Description : 다중 조건 처리
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/

#include<stdio.h>
// 매크로 상수 
#define LIMIT 30

int main(void) {
	int num = 0;

	for (num = 2; num <= LIMIT; num += 2) {
		printf("%d ", num);
	}
	printf("\n");

	// 2의 배수 합계 구하기
	int sum = 0;
	for (num = 2; num <= LIMIT; num += 2) {
		printf("%d ", num);
		sum += num;
	}
	printf("합계 : %d", sum);

}