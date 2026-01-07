#include<stdio.h>

int main(void) {
	char msg[] = "Good";
	int test[] = { 1,2,4,5 };
	char* p = msg;		



	// 배열이름을 포인터처럼 사용해보기
	printf("*p : %c, *msg : %s\n", *p, msg); // %s -> &배열이름[0] 자동 변환에서 종료문자까지
	printf("*p : %c, *msg : %c\n", *p, *msg); // %c -> &배열이름[0] 자동 변환. *&배열이름[0]

	printf("sizeof(msg) : %zu\n", sizeof(msg));
	printf("sizeof(p) : %zu\n", sizeof(p));



	
}