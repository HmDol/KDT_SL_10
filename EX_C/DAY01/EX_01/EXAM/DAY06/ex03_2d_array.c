/* ***************************************************
* Filename : ex03_2d_array.c
* Description :  2차원 배열의 행과 열 개수 계산
* Author : KHC
* HISTORY : 2026-01-05
*************************************************** */

#include<stdio.h>

// 실습 : 2차원 배열의
int main(void) {
	// 변수 선언 + 초기화
	int jumsu[5][3] = { 0 };
	const int ROWS = sizeof(jumsu) / sizeof(jumsu[0]);
	const int COLS = sizeof(jumsu[0]) / sizeof(int);

	printf("rows : %d / cols : %d\n", ROWS, COLS);
	//점수 입력
	for (int r = 0; r < ROWS; r++) {
		int scores[3] = { 0 };
		printf("%d번째 학생의 3과목 성적 입력(ex 100 90 80) : ", r+1);
		if (scanf("%d %d %d", &scores[0], &scores[1], &scores[2]) != 3) 
			printf("유효하지 않은 입력입니다.");
		else {
			for (int c = 0; c < COLS; c++) {
				jumsu[r][c] = scores[c];
			}
		}
	}

	// 입력 확인
	// 학생별 합계 및 평균 구하기
	for (int i = 0; i < ROWS; i++) {
		float sum = 0;
		for (int j = 0; j < COLS; j++) {
			sum += jumsu[i][j];
		}
		printf("총점수 : %.2f / 평균 : %.2f", sum, sum / COLS);
		printf("\n");
	}
	 
	for (int i = 0; i < COLS; i++) {
		float sum = 0;
		for (int j = 0; j < ROWS; j++) {
			sum += jumsu[j][i];
		}
		printf("%d 과목 총합: %.2f / 평균 : %.2f", i, sum, sum / COLS);
		printf("\n");
	}



	return 0;
}