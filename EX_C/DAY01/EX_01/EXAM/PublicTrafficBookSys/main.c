// 햄찬
#include "airplane.h"

// 재영
#include <stdio.h>
#include "ship_header.h"

// 영진
#include "train_header.h"

// 보경
#include <stdio.h>
#include <string.h>
#include "bus_header.h"


int main(void) {
	int inputNum = 0;
	int flag = 1;

	while (flag) {
		printf("============================ 대중 교통 통합 예약 SYS ==============================\n");
		printf("1. 기차 / 2. 비행기 / 3. 배 / 4. 버스\n");
		printf("선택(다른 키 누를 시 종료) : ");
		scanf("%d", &inputNum);
	
		switch (inputNum) {
		case 1: //영진
			trainStart();
			break;
		case 2: // 힘찬
			initialization();
			start();
			break;
		case 3: // 재영
			runShipSystem();
			break;
		case 4:
			busStart();
			break;
		default:
			printf("=====================================================================================\n");
			printf("                       전체 프로그램을 종료합니다!\n");
			printf("=====================================================================================");
			flag = 0;
			break;
		}
	}

    return 0;
}