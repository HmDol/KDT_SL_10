#pragma once

#ifndef INTEGRATION_H
#define INTEGRATION_H

#define MAX_SHIP 5
#define MAX_RES  30
// 구조체 정의 --------------------------------------------- 
// 선박명
// 출발지
// 도착지
// 출발시간
// 도착시간
// 총좌석 수
// 남은 좌석 수
// ---------------------------------------------------------
typedef struct {
    char name[20];
    char from[20];
    char to[20];
    char departTime[10];
    char arriveTime[10];
    int totalSeat;
    int remainSeat;
} Ship;

typedef struct {
    char user[20];
    int shipIndex;
} Reservation1;


// 함수  -----------------------------------------------------
/* 시스템 제어 */
void runShipSystem(void);

/* 출력 */
void showShipList(void);
void showReservations(void);

/* 예약 기능 */
void reserveTicket(void);
void cancelReservation(void);
//void updateReservation(void);

#endif
