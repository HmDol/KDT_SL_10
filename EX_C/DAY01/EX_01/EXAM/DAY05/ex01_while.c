/***************************************************
* Filename	  : ex01_while.c
* Description : while 반복문
*				반복 횟수가 정해진 경우 & 정해지지 않은 경우
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/

#include<stdio.h>

int main(void) {
	// 지역변수 선언 및 초기화
	int		  num = 1;
	const int LIMIT = 50;

	//반복용 변수 초기화
	num = 1;

	// while 반복문
	while (num <= LIMIT) {
		//if (num > 10) break;
		printf("num = %d\n", num++);

		//delay 용 코드
		for (int i = 0; i < 1000000000; i++);

	}


	return 0;
}


