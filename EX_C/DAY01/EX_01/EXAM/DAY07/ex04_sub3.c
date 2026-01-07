/* ***************************************************
* Filename : ex04 sub3.c
* Description : 다른 파일에 전역변수 사용
* Author : KHC
* HISTORY : 2026-01-06
*************************************************** */
#include<stdio.h>
#include "ex04_sub3.h"

extern int gv;

void printGv(void) {
	printf("printGv() - gv=%d\n", gv);
}


