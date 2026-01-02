/***************************************************
* Filename	  : ex09_switch_case.c
* Description : 다중 조건 처리
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int month = 0;

    printf("몇 월 ? ");
    if (scanf("%d", &month) != 1) {
        printf("유효하지 않은 입력입니다.\n");
        return 0;
    }

    switch (month) {
    case 12:
    case 1:
    case 2:
        printf("%d월은 겨울입니다.\n", month);
        break;

    case 3:
    case 4:
    case 5:
        printf("%d월은 봄입니다.\n", month);
        break;

    case 6:
    case 7:
    case 8:
        printf("%d월은 여름입니다.\n", month);
        break;

    case 9:
    case 10:
    case 11:
        printf("%d월은 가을입니다.\n", month);
        break;

    default:
        printf("1~12월만 입력하세요.\n");
        break;
    }

    return 0;
}