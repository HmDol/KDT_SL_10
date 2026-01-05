/* ***************************************************
* Filename : ex02_2d_array.c
* Description :  2차원 배열 선언 및 초기화
* Author : KHC
* HISTORY : 2026-01-05
*************************************************** */

#include<stdio.h>

int main(void) {
	// 변수 선언 + 초기화
	int arr1[2][3] = { {11,22,33}, {44,55,66} };
	int arr2[2][3] = { 11,22,33, 44,55,66 };

	int arr3[2][3] = { {11,22}, {44} };
	int arr4[2][3] = { 11,22,44 };

	// 원소확인
	for (int r = 0; r < 2; r++) {
		for (int c = 0; c < 3; c++) {
			printf("%d ", arr3[r][c]);
		}
		printf("\n");
	}


	return 0;
}