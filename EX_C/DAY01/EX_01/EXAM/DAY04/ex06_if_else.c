/***************************************************
* Filename : ex05_if.c
* Description : 단순 조건문
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/

#include<stdio.h>

int main(void) {
	// 짝수 & 홀수 출력
	int num = 8;
	if (num % 2) printf("%d 은 홀수\n", num);
	else printf("%d은 짝수\n", num);

	// 문자1개에 대한 대문자 & 소문자
	char c = 'c';
	if (c >= 97) printf("%c은 소문자", c);
	else printf("%c은 대문자", c);



}