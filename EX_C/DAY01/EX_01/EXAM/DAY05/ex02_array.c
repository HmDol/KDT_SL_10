/***************************************************
* Filename	  : ex02_array.c
* Description : 사용자 정의 함수
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

void main() {
	//지역변수 선언 및 초기화
	int score[5];

	//지역변수 초기화
	score[0] = 10;
	score[1] = 20;
	score[2] = 30;
	score[3] = 40;
	score[4] = 50;


	// 선언과 초기화 한번에 진행
	int age[10] = { 5, 19, 20, 45, 79, 100, 92, 35, 55, 99 };
	int num1[] = { 100, 200, 300 };
	int num2[10] = { 100, 200 };
	int num3[10] = { 0 };
	for (int i = 0; i < sizeof(score) / sizeof(score[0]); i++) {
		printf("score[%d] : %d\n", i, score[i]);
	}

	//선언 후 따로 초기화 시 {} 지원 안됨!!
	
	 
	
}

