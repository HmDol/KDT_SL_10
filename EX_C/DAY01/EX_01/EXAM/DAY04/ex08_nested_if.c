/***************************************************
* Filename	  : ex08_nested_if.c
* Description : 중첩 조건문, 조건문 안에 조건문
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/
# include <stdio.h>

int main(void) {
	int input = 0;

	// 입력받기
	printf("숫자하나 입력 : ");
	if (scanf("%d", &input) == 1) {
		if (input >= '0' && input <= '9') {
			printf("숫장비니다")
		}
	}
	else {
		printf("정확한 입력이 아닙니다!");
	}
	
}