/****************************************************
* Filename		: ex01_define.c
* Description	: #define 전처리기
*				  #연산자 -> 매개변수의 문자열 치환
*				  #연산자 -> 매개변수의 문자열 치환 -> 동적 식별자 문자열 생성
* History		: 2026-01-14
* Note
****************************************************/
#include < stdio.h>
#define print_int(x) printf(#x"=%d\n", x)
#define print_txt(txt) printf(#txt"\n")

int main(void) {
	int x = 5, y = 7;

	print_int(x);
	print_int(y);
	print_int(x + y);
	print_int(x + y - 2);
	print_txt(원하는 문장을 \n자유롭게 적으세요.);

	return 0;
}