/***************************************************
* Filename : ex03_assign_op.c
* Description : 대입 / 할당 연산자
*			    lvalue = rvalue;
*				lvlaue : 변수. 상수(리터럴상수, 심볼상수) 불가!
*				rvalue : 변수. 상수 모두 가능
*				복합대입연산자 : 대입연산자와 다른 연산자 결합한 것
*				lvalue 연산자= rvalue
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/

#include <stdio.h>

void main() {
	int num = 7;
	int result = 0;

	num = num + 10;
	num += 10;

	printf("num += 10 : %d \n", num);
}