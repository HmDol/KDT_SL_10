/* ***************************************************
* Filename : ex01_memory.c
* Description : 데이터와 메모리
*				낮은 주소(TEXT/CODE영역) ---- 높은 주소(STACK영역)
* Author : KHC
* HISTORY : 2026-01-06
*************************************************** */
#include <stdio.h>
#include <stdlib.h>

#define MAX 10000

const int constval = 30;	// 상수

int uninitial;				// 초기화 안된 전역변수
int initial = 30;			// 초기화 한 전역변수
static int staticval = 70;	// 정적변수

// --------------------------------------------------
// user define function
// --------------------------------------------------
int function() {
	return 20;
}

// --------------------------------------------------
// Entry Point Function
// --------------------------------------------------

int main(int argc, const char* argv[]) {
	//지역변수 선언 및 초기화
	int localval1 = 30;
	int localval2; 

	printf("숫자 입력: ");
	if (scanf("%d", &localval2));
	
	//동적 할당 변수
	char* arr = malloc(sizeof(char) * 10);

	//포인터 출력 영역
	printf("상수 Memory Address : \t\t %p \n", &constval);
	printf("비초기화 변수 Memory Address : \t % p \n", &uninitial);
	printf("초기화 변수 Memory Address : \t %p \n", &initial);
	printf("정적 변수 Memory Address : \t %p \n", &staticval);
	printf("함수 Memory Address : \t\t %p \n", function);
	printf("지역변수1 Memory Address : \t %p \n", &localval1);
	printf("지역변수2 Memory Address : \t %p \n", &localval2);
	printf("동적할당 변수 Memory Address : \t %p \n",arr);

	// 동적 할당 해제
	if (arr != NULL) free(arr);

	return 0;
	

}