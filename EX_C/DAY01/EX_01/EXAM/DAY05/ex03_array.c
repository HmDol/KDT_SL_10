/***************************************************
* Filename	  : ex03_array.c
* Description : 사용자 정의 함수
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

void main() {


	// 선언과 초기화 한번에 진행
	int score[10] = { 5, 19, 20, 45, 79, 100, 92, 35, 55, 99 };
	short nums[] = { 11,22,33,44,55,66,77,88,99,100,8,39,5,32,2,65,7,34,23,5,6,8,1 };
	
	int size_score = sizeof(score) / sizeof(score[0]);
	int size_nums = sizeof(nums) / sizeof(nums[0]);

	for (int i = 0; i < size_nums; i++) {
		if (i < size_score)
			printf("score[%d] : %d\n", i, score[i]);
		printf("nums[%d] : %d\n", i, nums[i]);
		printf("\n");

	}

	//선언 후 따로 초기화 시 {} 지원 안됨!!



}

