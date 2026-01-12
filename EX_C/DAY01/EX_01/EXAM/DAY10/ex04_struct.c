#include<string.h>
#include<stdio.h>

struct date {
	int year;
	int month;
	int day;
};

struct userScore {
	char userId[8];
	//int score;
	//int rank;
	struct date inputDate;
	struct date changeDate;
};

typedef struct userScore UserScore;

int main(void) {
	//변수 선언 및 초기화
	UserScore s1 = { "s1", {2026, 1,1}, {2026, 2,1} };
	UserScore s2 = s1;
	UserScore* pS = &s1;


	// 사용자 정보 확인 출력 - 구조체에 직접 접근
	printf("[s1, 직접접근]id:%s, in : %d-%d-%d, change : %d-%d-%d\n",
		s1.userId,
		s1.inputDate.year, s1.inputDate.month, s1.inputDate.day,
		s1.changeDate.year, s1.changeDate.month, s1.changeDate.day);

	// 사용자 정보 확인 출력 - 구조체 포인터로 간접 접근
	printf("[s1, 간접접근] id:%s, in : %d-%d-%d, change : %d-%d-%d\n",
		pS->userId,
		pS->inputDate.year, pS->inputDate.month, pS->inputDate.day,
		pS->changeDate.year, pS->changeDate.month, pS->changeDate.day);



	// 사용자 정보 변경
	//s1.userId = "newId" // <= 배열 선언과 동시에 초기화시에만 가능
	strcpy(s1.userId, "newID");
	s1.inputDate.year = 2025;
	s1.inputDate.month = 1;
	s1.inputDate.day = 12;

	printf("[s1] id:%s, in : %d-%d-%d, change : %d-%d-%d\n",
		s1.userId,
		s1.inputDate.year, s1.inputDate.month, s1.inputDate.day,
		s1.changeDate.year, s1.changeDate.month, s1.changeDate.day);

	return 0;

}