#include <stdio.h>
#include "bus_header.h"

// 데이터
Bus bus[5] = {
    {"대구", "서울", 9, 4, 25000, 10 },
    {"부산", "영천", 14, 3, 15000, 8 },
    {"포항", "청주", 20, 4, 25000, 1 },
    {"강릉", "대전", 11, 4, 22000, 7 },
    {"서울", "대전", 5, 3, 12000, 0 }
};

Reservation res = { 0, 0, 0, -1 };

//================================================
// 메인 메뉴 출력 : showMenu()
//================================================
void showMenu()
{
    printf("\n");
    printf("   _____________________________\n");
    printf("  |    BUS RESERVATION SYSTEM   |\n");
    printf("  |-----------------------------|\n");
    printf("  |  []  []  []  []  []  []     |\n");
    printf("  |                             |\n");
    printf("  |          보경 버스          |\n");
    printf("  |_____________________________|\n");
    printf("     (O)                  (O)    \n");
    printf("\n");
    printf("1. 버스 노선 조회\n");
    printf("2. 버스 예약\n");
    printf("3. 예약 확인\n");
    printf("0. 프로그램 종료\n");
}


//================================================
// 함수 이름 : busSearch()
// 함수 기능 : 출발지 도착지 입력 후 
//             노선의 출발 시간, 소요시간, 요금, 잔여 좌석 출력
// 매개 변수 : 없음 
// 결과 반환 : 노선 정보 출력(시간/요금/잔여 좌석)
//================================================
void busSearch()
{
    printf("\n");
    printf("▶ 전체 노선 정보\n");

    for (int i = 0; i < 5; i++)
    {
        printf("%s → %s | 출발: %02d시 | 소요 시간: %d시간 | 요금: %d원 | 잔여 좌석: %d석\n",
            bus[i].depart, bus[i].arrive, bus[i].time,
            bus[i].duration, bus[i].price, bus[i].seats);
    }
}
//================================================
// 함수 이름 : busReserve()
// 함수 기능 : 출발지/도착지 입력 -> 버스 조회 -> 
//             좌석 충분 -> 버스 예약 -> 에약 정보 저장 및 예약 번호 출력 
// 매개 변수 : 없음
// 결과 반환 : 예약 완료 및 예약 번호 출력
//================================================
void busReserve()
{

    char de[10], ar[10];
    int people;
    static int reserveCnt = 0;        // static : 함수 끝나도 메모리에 유지 -> 예약 번호 누적 증가

    printf("\n");
    printf("▶ 버스 예약\n");

    printf("출발지 입력 : ");
    scanf("%s", &de);

    printf("도착지 입력 : ");
    scanf("%s", &ar);


    for (int i = 0; i < 5; i++)
    {
        if (strcmp(de, bus[i].depart) == 0 && strcmp(ar, bus[i].arrive) == 0)       // de = 버스 노선이랑 동일하면 0
        {
            printf("인원 수 입력: ");
            scanf("%d", &people);

            if (people <= 0)
            {
                printf("잘못된 인원 수 입니다.\n");
                return;
            }

            if (bus[i].seats < people)
            {
                printf("좌석 부족\n");
                return;
            }

            printf("\n[버스 좌석]\n");
            for (int s = 0; s < 10; s++)
            {
                if (bus[i].seatStatus[s] == 0)
                    printf("%2d:빈 | ", s + 1);
                else
                    printf("%2d:예약 | ", s + 1);

                if ((s + 1) % 5 == 0) printf("\n");  // 5석씩 줄바꿈
            }

            // 좌석 선택
            int seatNum;

            for (int p = 0; p < people; p++)
            {
                printf("좌석 선택 (1~10) : ");
                scanf("%d", &seatNum);

                if (seatNum < 1 || seatNum > 10 || bus[i].seatStatus[seatNum - 1] == 1)
                {
                    printf("이미 예약된 좌석입니다.\n");
                    p--;
                }
                else
                {
                    bus[i].seatStatus[seatNum - 1] = 1;
                    res.seatNumbers[p] = seatNum;
                }
            }

            bus[i].seats -= people;                     // 좌석 수 
            reserveCnt++;                         // 예약 번호 추가
            res.number = reserveCnt;              // 예약 번호
            res.people = people;                        // 인원 수
            res.totalPrice = people * bus[i].price;     // 총 금액
            res.busIndex = i;                           // 버스 노선

            printf("\n예약 완료!\n예약 번호: %d\n", res.number);
            return;
        }
    }

    printf("해당 노선 없음\n");
}


//================================================
// 함수 이름 : reserveCheck()
// 함수 기능 : 예약 번호 입력 받고 예약 확인 및 출력
// 매개 변수 : 없음
// 결과 반환 : 예약 정보 출력(노선/인원/총 금액)
//================================================
void reserveCheck()
{
    int num;

    printf("\n");
    printf("▶ 예약 확인 기능\n");

    printf("▶ 예약 번호 입력 : ");
    scanf("%d", &num);

    if (num == res.number && res.busIndex != -1)    // -1이면 예약 없는 상태임
    {
        int i = res.busIndex;
        printf("\n▶ 예약 정보\n");
        printf("노선 : %s → %s \n", bus[i].depart, bus[i].arrive);
        printf("출발 시간 : %02d시 \n", bus[i].time);
        printf("인원 : %d명 \n", res.people);
        printf("좌석 번호 : ");
        for (int j = 0; j < res.people; j++)
        {
            printf("%d ", res.seatNumbers[j]);
        }
        printf("금액 : %d원 \n", res.totalPrice);
        printf("\n");

    }
    else
    {
        printf("예약 정보가 없습니다.\n");
    }
}

//================================================
// 함수 이름 : exitProgram
// 함수 기능 : 프로그램 종료
// 매개 변수 : 없음
// 결과 반환 : 없음
//================================================
void exitProgram()
{
    printf("프로그램 종료");
    exit(0);

}


void busStart() {
    int menu = -1;

    while (1)
    {
        showMenu();
        printf("원하는 메뉴 번호 입력 ▶ ");
        scanf("%d", &menu);

        switch (menu)
        {
        case 1:
            busSearch();
            break;

        case 2:
            busReserve();
            break;

        case 3:
            reserveCheck();
            break;

        case 0:
            return 0;
            break;

        default:
            printf("잘못된 접근 입니다.");
        }
    }
}

