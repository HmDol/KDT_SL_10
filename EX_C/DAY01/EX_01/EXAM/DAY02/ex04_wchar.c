/****************************************************
* Filename		: ex04_wchar.c
* Description	: 확장문자형 타입
*				  ASCII코드 제외한 기업/국가에서 추가한 무자 저장 타입
*				  Window는 2바이트에 저장 / Linux는 4바이트에 저장
* History		: 2025.12.29 by hc
* Note
****************************************************/
// 라이브러리 로딩
#include <stdio.h>
#include <wchar.h>
#include <locale.h>

// 엔트리 포인트 함수 : os에서 실행 시 호출하는 함수
void main() {
	wchar_t wch = L'가';
	setlocale(LC_ALL, "Korean");
	const char* loc = setlocale(LC_ALL, "");


	printf("wchar => %lc\n", wch); // 확장 문자형 출력 안됨
	printf("setlocale => %ls\n", loc);
	//wprintf(L"wchar => %lc\n", wch);

}