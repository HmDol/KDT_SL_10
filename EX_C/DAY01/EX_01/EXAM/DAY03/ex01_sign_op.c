/****************************************************
* Filename		: ex01_sign_op.c
* Description	: 단항 연산자 -> 부호 연산자
*				  - 부호 연산자 : 현재 부호를 반대로 변환
*				  + 부호 연산자 : 변환 없음
*				  ★ 컴파일러의 자동형변환 적용
*				     타입별 기본타입으로 형변환 진행
* History		: 2025.12.29 by hc
* Note
****************************************************/
#include <stdio.h>

int main(void) {
	//지역변수 선언
	int		i, j;
	short	s;

	//지역변수 초기화
	i = -10;
	i = +i;
	j = -10;
	j = -j;

	printf("i => %d sizeof(i) => %d\n", i, sizeof(i));
	printf("j => %d sizeof(j) => %d\n", i, sizeof(j));

	//지역변수 초기화 및 값 확인
	s = -7;
	printf("s => %d sizeof(s) => %d\n", s, sizeof(s));
	printf("+s => %d sizeof(+s) => %d\n", +s, sizeof(+s));



}