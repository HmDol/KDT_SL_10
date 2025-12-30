/****************************************************
* Filename		: ex01_sign_op.c
* Description	: 단항 연산자 -> 증감 연산자
*				  -- 연산자 : 현재 값 - 1
*				  ++ 연산자 : 현재 값 + 1
*				  ★ 변수값을 변경하는 연산자
* History		: 2025.12.29 by hc
* Note
****************************************************/


// 라이브러리 로딩
#include <stdio.h>
#include <string.h>

// 엔트로피포인트 함수
int main(void) {
	char str[] = "abc";

	printf("\"abc\"==\"abc\" ? %dn ", "abc" == "abc");
	printf(" str == \" abc\"? %d\n");
	printf("strcmp(str,\"abc\") ? %d \n", strcmp(str, "abc"));
	printf("strcmp(str,\"abb\") ? %d \n", strcmp(str, "abb"));
	printf("strcmp(str,\"abd\") ? %d \n", strcmp(str, "abd"));

	return 0;


}