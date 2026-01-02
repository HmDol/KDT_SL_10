/***************************************************
* Filename : ex02_condition_op.c
* Description : 조건부 연산자 / 삼항 연산자
*			    (조건) ? 결과(참) : 결과(거짓)
*				참	 : 비교/논리 => 1, 0이 아닌값
*				거짓 : 비교/논리 => 0 
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/

#include <stdio.h>

int main(void) {
	//지역변수 선언 및 초기화
	int result = 0, n1 = 0, n2 = 0;
	int score = 85;
	char grade = ' ';
	
	//학점 출력하기 => 90이상 A, 80이상 B, 나머지는 C
	grade = (score >= 90) ? 'A' : (score >= 80) ? 'B' : 'C';
	printf("%d점은 %c등급입니다.\n", score, grade);


	// 연산결과 출력
	result = (n1 == n2) ? 100 : -100;

	printf("n1=%d, n2=%d, result=%d\n", n1, n2, result);

	return 0;
}