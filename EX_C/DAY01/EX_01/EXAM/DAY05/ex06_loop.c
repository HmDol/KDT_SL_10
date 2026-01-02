/***************************************************
* Filename	  : ex04_while.c
* Description : while 반복문
*				반복 횟수가 정해진 경우 & 정해지지 않은 경우
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 실습 UP/DOWN 게임 만드릭
// 프로그램 지정 숫자 준비
// 사용자가 입력한 숫자
// 입력 숫자와 지정 숫자 비교해서 정보 제공 : UP/DOWN
// 입력 숫자와 지정 숫자 동일하면 종료

int main(void) {
	
	for (int i = 0; ; i++) {
		printf("무한 반복 1- %d\n", i);
	}
	for (;;) {
		printf("무한 반복 2");
	}
	while (1) {
		printf("무한 반복 3");
	}


	return 0;
}

