/***************************************************
* Filename	  : ex04_while.c
* Description : while 반복문
*				반복 횟수가 정해진 경우 & 정해지지 않은 경우
* Author	  : KHC
* History	  : 2026-01-02
*****************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 실습 UP/DOWN 게임 만드릭
// 프로그램 지정 숫자 준비
// 사용자가 입력한 숫자
// 입력 숫자와 지정 숫자 비교해서 정보 제공 : UP/DOWN
// 입력 숫자와 지정 숫자 동일하면 종료

int main(void) {
	// 지역 변수 선언
	int answer, cnt =0;
	
	printf("숫자를 하나 지정해주세요 : ");
	scanf("%d", &answer);
	printf("\n\n\n=====================게임 시작=========================\n");
	while(1) {
		int input;
		printf("숫자 입력 : ");
		scanf("%d", &input);
		
		if (input > answer) {
			printf(">> Down!\n\n");
			cnt++;
		}
		else if (input < answer) {
			printf(">>UP\n\n");
			cnt++;
		}
		else break;
		
	}
	printf("\n\n %d 정답입니다!!", answer);
	printf("\n%d번만에 맞추셨습니다!\n\n", cnt);
	printf("===========================게임 끝===============================");
	


	return 0;
}

