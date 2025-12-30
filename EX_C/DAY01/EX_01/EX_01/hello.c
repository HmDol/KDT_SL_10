/*************************************
	파일명 : hello.c
	설  명 : C 프로그램 기본 구조 이해
	작  성 : 2025. 12. 06. So
			 2025. 12. 07. Hong
**************************************/
# include <stdio.h>

/* -----------------------------------
	FNAME : main 
	FDESC : entry point
	PARAM : void
	RETURN: int 0 exit code
----------------------------------- */

int main(void){

	// 표준 출력 printf -------------
	printf("정수 : %d\n", 100);
	printf("실수 : %f\n", 8.9);
	printf("문자 : %c\n", 'A');
	printf("문자열 : %s\n", "ABC");
	printf("hello c");
	return  0;
}