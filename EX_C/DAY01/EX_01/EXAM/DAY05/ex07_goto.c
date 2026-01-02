/***************************************************
* Filename	  : ex04_while.c
* Description : while 반복문
*				반복 횟수가 정해진 경우 & 정해지지 않은 경우
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/


#include <stdio.h>
void main() {
	printf("시작\n");
	
	goto JUMP;

	printf("이 문장은 실행 x");
JUMP:
	printf("JUMP 라벨로 이동했습니다.\n");

	return 0;

}
