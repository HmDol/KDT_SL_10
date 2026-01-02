/***************************************************
* Filename	  : ex04_while.c
* Description : while 반복문
*				반복 횟수가 정해진 경우 & 정해지지 않은 경우
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/

#include<stdio.h>

// 반복 중단 실습
int main(void) {
	// 지역변수 선언 및 초기화
	int sum = 0, flag = 1;

	printf("숫자 합산 (종료는 0입력)");

	while (flag) {
		int num = 0;
		printf(">>");
		scanf("%d", &num);

		//if (num == 0)
		//	flag = 0;
		//else
		//	sum += num;
		(num == 0) ? (flag = 0) : (sum += num);
	}
	printf("숫자 합 : %d\n", sum);

	return 0;
}


