/* ***************************************************
* Filename : ex03_local_global.c
* Description : 데이터와 메모리
*				낮은 주소(TEXT/CODE영역) ---- 높은 주소(STACK영역)
* Author : KHC
* HISTORY : 2026-01-06
*************************************************** */

#include <stdio.h>

int gMax = 1000;
const int G_MIN = 10;

int main(void) {
	//지역변수
	int iValue = 7;
	int gMax = 9;

	{
		int x = 10, y = 20;
		int iValue = 2000;

		printf("[블록] x = %d, y=%d, iValue = %d, gMax = %d\n", x, y, iValue, gMax);
	}
	// main 함수 : 전역변수, 상수, 지역변수 접근
	// 지역변수 초기화 x
	//printf("[메인] iValue = %d\n", iValue);

	// main 함수 : 다른 블록 안의 지역 변수 접근 불가
	//printf("[메인] x = %d, y=%d\n", x, y);

	// 선언 및 초기화 전 지역변 수
	printf("[메인] test = %d\n", test);

	int test = 77;
	printf("[메인] test = %d\n", test);

	return 0;

}