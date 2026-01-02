/***************************************************
* Filename : ex04_if.c
* Description : 단순 조건문
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/

#include<stdio.h>

void main() {
	int num = 7;

	// 조건에 따른 출력 : 짝수여부에 따른 출력
	if (num % 2 == 0) {
		printf("%d 짝수\n", num);
	}
	else {
		printf("%d 홀수", num);
	}
}