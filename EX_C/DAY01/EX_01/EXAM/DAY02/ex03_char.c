/****************************************************
* Filename		: ex03_char.c
* Description	: 문자형 타입
*				  1바이트 정수 저장
*				  '문자1개' 입력 시 해당 코드값이 저장
*				  limiits.h 에서 문자형 타입의 최소/최대값 선언
*				  ASCII코드표 기반 변환 진행
* History		: 2025.12.29 by hc
* Note
****************************************************/
// 라이브러리 로딩
#include <stdio.h>
#include <limits.h>

// 엔트리 포인트 함수 : os에서 실행 시 호출하는 함수
void main() {
	unsigned char code  = ' ';	//문자형 초기화 시에''만 지정 X
	unsigned char code2 = 0;		//문자형 초기화 시에 숫자 지정 가능
	printf("code값 : %c, %d, %x\n", code, code, code);

	code = -1;
	printf("code값 : %c, %d, %x\n", code, code, code);

}