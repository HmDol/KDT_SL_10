#include "1016_work_김힘찬_header.h"
#include <stdio.h>

// 6- 18
int score[STU + 1][SUB + 1] = {
	{ 100, 100, 100 },
	{ 25,  20,  20  },
	{ 35,  30,  30  },
	{ 45,  40,  40  }
};

void sumScore(void) {
	int i, j;
	for (i = 0; i < STU; i++)
		for (j = 0; j < SUB; j++) {
			score[i][SUB] += score[i][j];
			score[STU][j] += score[i][j];
		}
}


void printScore(void) {
	int i, j;
	printf("번호 국어 영어 수학 총점  평균\n");
	printf("===============================\n");

	for (i = 0; i < STU; i++) {
		printf(" %d   ", i + 1);

		for (j = 0; j < SUB; j++)
			printf("%3d  ", score[i][j]);

		printf(" %3d  %5.1f\n", score[i][SUB], score[i][SUB] / (float)SUB);
	}
	printf("===============================\n총점 ");

	for (j = 0; j < SUB; j++)
		printf("%3d  ", score[STU][j]);

	puts("");
}



// 6 - 8
int multiply(int x, int y) {
	int result = x * y;

	return result;
}

int getUserInput(void) {
	int num;

	printf("input a number(2~9) :");
	scanf("%d", &num);

	return num;
}

void printGugudan(int dan) {
	int i;

	for (i = 1; i <= 9; i++) {
		int result = multiply(dan, i); // int multiply(int x, int y)를 호출         
		printf("%d*%d=%2d\n", dan, i, result);
	}
}

void printGugudanAll(void) {
	int i, j;

	for (i = 1; i <= 9; i++) {
		for (j = 2; j <= 9; j++) {
			printf("%d*%d=%2d ", j, i, multiply(j, i));
		}
		printf("\n");
	}
}


// ex05
void func1(void) {
	static int sv2 = 1; //생성된 후 1회 초기화, 메모리 유지, 해당 함수에서만 사용가능
	int lv = 1;
	printf("[func1] sv2=%d, lv=%d\n", sv2++, lv++);
}

void func2(void) {
	int sv = 100;
	printf("[func2] sv = %d\n", sv);
	//printf("[func2] static 지역변수 sv2=%d\n", sv2);
}