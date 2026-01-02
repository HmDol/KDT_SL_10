/***************************************************
* Filename	  : ex09_switch_case.c
* Description : 다중 조건 처리
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/
#include <stdio.h>
//#define _CRT_SECURE_NO_WARNINGS
// 점수입력 받으면 학점 출력
int main(void) {
    int score = 0;
    char grade = 0;

    printf("점수 입력 : ");
    if (scanf("%d", &score) != 1) {
        printf("입력이 올바르지 않습니다.");
        return 0;
    }

    /*if (score >= 90)
        grade = 'A';
    else if (score >= 80)
        grade = 'B';
    else if (score >= 70)
        grade = 'C';
    else if (score >= 60)
        grade = 'D';
    else
        grade = 'F';

    printf("당신의 학점은 %c 입니다.", grade);
    return 0;*/

    // 점수 범위 체크
    if (score < 0 || score > 100) {
        printf("점수는 0 ~ 100 사이여야 합니다.");
        return 0;
    }

    switch (score / 10) {
    case 10:            // 100점
    case 9:             // 90~99
        grade = 'A';
        break;
    case 8:             // 80~89
        grade = 'B';
        break;
    case 7:             // 70~79
        grade = 'C';
        break;
    case 6:             // 60~69
        grade = 'D';
        break;
    default:            // 0~59
        grade = 'F';
        break;
    }

    return 0;
}
