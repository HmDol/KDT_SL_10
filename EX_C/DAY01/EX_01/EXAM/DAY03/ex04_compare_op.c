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
	//지역변수 선언 및 초기화
	int n1 = 10, n2 = 20;
	float f1 = 10.0f, f2 = 20.0f;
	double d1 = 10.0, d2 = (double)f2;

	//1. 정수 비교 연산 : >, < , >=, <=, ==, !=
	printf("%d > %d : %d\n", n1, n2, n1 > n2);
	printf("%d < %d : %d\n", n1, n2, n1 < n2);
	printf("%d <= %d : %d\n", n1, n2, n1 <= n2);
	printf("%d >= %d : %d\n", n1, n2, n1 >= n2);
	printf("%d == %d : %d\n", n1, n2, n1 == n2);
	printf("%d != %d : %d\n", n1, n2, n1 != n2);


	//2. 실수 비교 연산


}