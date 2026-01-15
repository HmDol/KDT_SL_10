#pragma once
#ifndef bus_header_h
#define bus_header_h

//================================================
// 구조체 정의 
//================================================
typedef struct {
    char depart[10];    // 출발지 입력
    char arrive[10];    // 도착지 입력
    int time;           // 출발 시간
    int duration;       // 소요 시간
    int price;          // 요금
    int seats;          // 잔여 좌석
    int seatStatus[10]; // 0 : 빈자리, 1 : 예약된 자리
} Bus;

typedef struct {
    int number;     // 예약 번호
    int people;     // 예약 인원
    int totalPrice; // 총 금액
    int busIndex;   // 예약한 버스 인덱스
    int seatNumbers[10];    // 예약한 좌석 번호
} Reservation;


//================================================
// 함수 선언
//================================================
void showMenu();
void busSearch();
void busReserve();
void reserveCheck();
void exitProgram();
void busStart();

#endif