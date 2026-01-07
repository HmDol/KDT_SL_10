#pragma once
#ifndef SCORE_H			// 해더의 중복 정의를 방지하기 위한 코드, 시작지점
#define SCORE_H			// 의미 : 만약 not define(정의되어 잇지 않다면)이면 define해라

#define STU 4
#define SUB 3

extern int score[STU + 1][SUB + 1];

//6-18
void sumScore(void);
void printScore(void);

// 6-8
int  multiply(int x, int y);
int  getUserInput(void);
void printGugudan(int dan);
void printGugudanAll(void);



#endif					// 끝지점
