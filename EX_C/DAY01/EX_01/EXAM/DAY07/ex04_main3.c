/* ***************************************************
* Filename : ex04_main3.c
* Description : 다른 파일에 전역변수 사용
* Author : KHC
* HISTORY : 2026-01-06
*************************************************** */
#include <stdio.h>
#include <stdlib.h>
#include "ex04_sub3.h"

int gv = 100;

int main(void) {
	printf("main() - gv = %d\n", gv);
	printGv();

	return 0;
}