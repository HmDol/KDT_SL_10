/***************************************************
* Filename	  : ex05_array.c
* Description : 배열
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

void main() {
	// 선언 및 초기화 
	int score[5] = { 0 };
	int sum = 0;
	float avg = 0;
	const int LEN = sizeof(score) / sizeof(score[0]);
	

	// 배열 값 입력 받아서 저장
	for (int i = 0; i < LEN; i++) {
		printf("초기값 입력");
		scanf("%d", &score[i]);
	}

	for (int i = 0; i < LEN; i++) {
		sum += score[i];
	}
	printf("합계 : %d , 평균 : %f\n", sum, (float)sum / LEN);


}

