/********************************************************************
* filename : ex03_input.c
* Description : 표준 입력 



*********************************************************************/
#pragma warning(disable:4996)
# include <stdio.h>

int main(void) {
	

	// 입력데이터 저장용 변수 : 지역변수
	int age = 0;
	

	// 변수 주소 출력
	printf("age 변수 주소 : %d / %p", &age, &age);


	// 키보드로 입력 받은 데이터 저장 및 확인

	printf("\n나이 입력 받기 : ");
	if (scanf("%d", &age) != 1)
		return 0;


	printf("당신의 나이는 %d 입니다.", age);

}