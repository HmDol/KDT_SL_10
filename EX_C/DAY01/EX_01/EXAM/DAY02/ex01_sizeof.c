/****************************************************
* Filename		: ex01_sizeof.c
* Description	: C언어에서 자료형별 사용 메모리 크기 확인
* History		: 2025.12.29 by hc
* Note
****************************************************/
// 라이브러리 로딩
#pragma warning(disable:4996)
#include <stdio.h>

// 엔트리 포인트 함수 : os에서 실행 시 호출하는 함수
void main() {
	short sh = 12;        // short 정수형 변수
	int nt = 155;         // int 정수형 변수
	long long on = 1666;  // long long 정수형 변수

	printf("자료형의 크기를 알아보는 코드 \n");

	printf("1. short : %dbyte, %dbyte \n", sizeof(sh), sizeof sh);
	printf("2. int : %dbyte, %dbyte \n", sizeof(nt), sizeof nt);
	printf("3. long long : %dbyte, %dbyte \n", sizeof(on), sizeof on);

}