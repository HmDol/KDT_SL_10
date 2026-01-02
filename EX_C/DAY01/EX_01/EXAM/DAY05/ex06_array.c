/***************************************************
* Filename	  : ex05_array.c
* Description : 배열
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>

// 함수이름 : printArray
// 함수기능 : 배열의 원소들을 출력해주는 함수
// 매개변수 : int arr[], 원소개수 nLen
// 반환값 : void

void printArray(int arr[], int nLen) {
	for (int i = 0; i < nLen; i++) {
		printf("%d요소 - %d", i, arr[i]);
	}
}

int getSum(int arr[], int nLen) {
	int sum = 0;
	for (int i = 0; i < nLen; i++) {
		sum += arr[i];
	}
	return sum;
}

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

	printArray(score, LEN);
	printf("합계 : %d , 평균 : %f\n", getSum(score, LEN), (float)sum / LEN);


}

