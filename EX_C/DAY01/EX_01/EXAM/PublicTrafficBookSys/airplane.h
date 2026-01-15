#pragma once
#ifndef AIRLINE_H
#define AIRLINE_H

#include <stdio.h>
#include <string.h>

// ======================= 상수 =======================
#define MAX_MEMBERS   10
#define MAX_PLANES    20
#define MAX_BOOKINGS  200

#define SEAT_ROWS 14
#define SEAT_COLS 4
#define SEATS_TOTAL (SEAT_ROWS * SEAT_COLS)

// ----------------------- 구조체 -----------------------------------
typedef struct member {
    char memId[30];
    char name[30];
    char phone_num[30];
} Member;

typedef struct airplan {
    int fly_id;             // 비행번호
    char origin[30];        // 출발지
    char destination[30];   // 목적지
    int departure_time;     // 출발시간
    int arrival_time;       // 도착시간
    int cost;               // 가격
    int seats[SEAT_ROWS][SEAT_COLS]; // 좌석 (0=미예약, 1=예약)
    int seat_num;           // 잔여석 (0의 개수)
} Plane;

typedef struct book {
    int book_id;
    int member_index;   // 로그인 회원 index
    int plane_index;    // planeArr index
    int row;            // 0~13
    int col;            // 0~3
} Book;

// ---------------------- 전역 변수 (extern 선언) ---------------------------------
extern Member memArr[MAX_MEMBERS];
extern Plane  planeArr[MAX_PLANES];
extern Book   bookArr[MAX_BOOKINGS];

extern int bookCount;
extern int currentLoginIndex;

// ======================= 함수 선언 (프로토타입) =======================
void initialization(void);
void initSeats(Plane* p);

void start(void);
void login(void);
void addMember(void);

void selectPrint(void);
void printMember(Member m);

void printAirPlaneList(void);
void logout(void);

void printSeats(int planeIndex);
void printAirPlaneTableOnly(void);

void reserve(void);
void showMyBookings(void);

int  findPlaneIndexByFlyId(int flyId);
int  colFromChar(char seatCol);
void printSeatMapFromPlaneIndex(int planeIndex);

void clearLine(void);
void pauseEnter(void);
void printTitle(const char* title);
void printDivider(void);

#endif // AIRLINE_H
