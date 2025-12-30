// filename : ex02.input.c
// description : 표준 입력 함수


#pragma warning(disable:4996)
# include <stdio.h>

int main(void) {
	printf("나이 입력 받기 : ");

	//입력받기
	int age = 0;
	scanf("%d", &age);
	
	// 입력 확인
	printf("당신의 나이는 %d입니다.", age);
	
}