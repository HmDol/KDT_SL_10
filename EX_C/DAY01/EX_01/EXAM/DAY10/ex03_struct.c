#include<stdio.h>
#include<string.h>

//user define type
// - 회원 타입 구조체
// * 아이디, 비번, 이름, 나이, 생년월일(날짜타입 - 년월일)

struct date {
	int year;
	int month;
	int day;
};

typedef struct member {
	char userId[10];
	char userPw[10];
	char userName[10];
	int age;
	struct date birth;
}Mem;

// 회원은 2명
//	- 1번째 회원 : 생성과 동시에 초기화
//	- 2번째 회원 : 입력받은 정보로 저장

int main(void) {
	Mem m1 = { "abc123", "pw123", "kim", 20, {2007, 10, 2} };
	Mem m2;

	printf("[m1] %s / %s / %s / %d / (%d %d %d)\n", 
		m1.userId, m1.userPw, m1.userName, m1.age, 
		m1.birth.year, m1.birth.month, m1.birth.day);
	char userId[10];
	char userPw[10];
	char userName[10];
	int age;
	struct date birth;


	printf("회원 아이디 입력 : ");
	scanf("%9s", userId);
	printf("회원 비밀번호 입력 : ");
	scanf("%9s", userPw);
	printf("회원 이름 입력 : ");
	scanf("%9s", userName);
	printf("회원 나이 입력 : ");
	scanf("%d", &age);
	printf("회원 생년월일 입력 (2025 1 1) : ");
	scanf("%d %d %d", &birth.year, &birth.month, &birth.day);
	
	strcpy(m2.userId, userId);
	strcpy(m2.userPw, userPw);
	strcpy(m2.userName, userName);
	m2.age = age;
	m2.birth = birth; 

	
	printf("[m2] %s / %s / %s / %d / (%d %d %d)", 
		m2.userId, m2.userPw, m2.userName, m2.age, 
		m2.birth.year, m2.birth.month, m2.birth.day);






	return 0;
}