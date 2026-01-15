#pragma once
#ifndef TOTAL_H
#define TOTAL_H

#include <stdio.h>
#include <string.h>

#define TIME 6
#define LOC 15
#define NAME 5
#define PHONE 14
#define SEATNUM 40
#define MAXCUSTOMER 10
#define MAXTRAIN 5


// 구조체
struct train
{
	int t_num;
	char t_time[TIME];
	char start[LOC];
	char end[LOC];
	int seat[SEATNUM];
};
typedef struct train Train;

struct customer
{
	int id;
	int pw;
	char name[NAME];
	char phone[PHONE];
};
typedef struct customer Customer;


// 전역 배열
extern Customer customers[MAXCUSTOMER];
extern int Ccount;

extern Train trains[MAXTRAIN];


// 함수
void signup(void);
Customer* trainlogin(void);

void train(const char* end);
void trainlist(const char* end);
void trainseat(Train* t);
void trainStart();
#endif