/***************************************************
* Filename	  : ex04_array.c
* Description : 사용자 정의 함수
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

void main() {

	char ch[10];

	//입력받아서 
	printf("10개로 구성된 문자열 입력 : ");
	scanf("%9s", ch);

	printf("array ch : %s\n", ch);
	return 0;
}

