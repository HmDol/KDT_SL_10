/****************************************************
* Filename		: ex06_casting.c
* Description	: 형변환
*				  자동 형변환 ==> 시스템에서 처리
*				  명시적형변환 => (타입명) 변수명
* History		: 2025.12.29 by hc
* Note
****************************************************/
// 라이브러리 로딩
#include <stdio.h>			// 입출력 함수들

// 매크로 상수
#define WIDTH 100			// 전처리기/컴파일러에 의해 모두 치환

// 엔트리 포인트 함수 : os에서 실행 시 호출하는 함수
void main() {
	int value = 12, no = 9;
	char ch = 65;
	// -> 연산시 자동형변환 진행 : int/int => int
	// -> 명시적 형변환 : double/int
	// -> 묵시적 형변환 : double/double => double
	printf("%d / %d = %f\n", value, no, (double)value / no);

	printf("ch : %c, %c\n", ch, (char)65);
}