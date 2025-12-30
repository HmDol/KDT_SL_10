/****************************************************
* Filename		: ex01_sign_op.c
* Description	: 단항 연산자 -> 증감 연산자
*				  -- 연산자 : 현재 값 - 1
*				  ++ 연산자 : 현재 값 + 1
*				  ★ 변수값을 변경하는 연산자
* History		: 2025.12.29 by hc
* Note
****************************************************/

#include <stdio.h>

int main()
{
	int a = 5;
	int b = 3;
	int result;

	result = a * b + (++a);
	printf("결과 = %d\n", result);

	int c = 6;
	int d = 4;

	result = c * d + (c--);
	printf("결과 = %d\n", result);

	return 0;
}
