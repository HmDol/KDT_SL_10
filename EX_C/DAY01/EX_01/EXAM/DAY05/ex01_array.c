/***************************************************
* Filename	  : ex01_array.c
* Description : 사용자 정의 함수
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

// 변수와 배열 차이 이해
// => 30명의 점수를 저장 및 출력

void main() {
	//지역변수 선언 및 초기화
	int score[5];

	//지역변수 초기화
	score[0] = 10;
	score[1] = 20;
	score[2] = 30;
	score[3] = 40;
	score[4] = 50;
	
	for( int i = 0; i < sizeof(score)/sizeof(score[0]); i++){ 
		printf("score[%d] : %d\n", i, score[i]);
	}
}

