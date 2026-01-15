#include"airplane.h"

// ======================= 전역 함수 =======================
Member memArr[10] = { 0 };
Plane  planeArr[20] = { 0 };
Book bookArr[200] = { 0 };

int  bookCount = 0;
int currentLoginIndex = -1; // 로그인 맴버 인덱스 값



// ======================= 함수 정의 =======================

void clearLine(void) {
    while (getchar() != '\n'); // 입력 버퍼 정리
}

void pauseEnter(void) {
    printf("\n[Enter]를 누르면 돌아갑니다...");
    clearLine();
    getchar();
}

void printDivider(void) {
    printf("\n===============================================================================\n");
}

void printTitle(const char* title) {
    printDivider();
    printf("  %s\n", title);
    printDivider();
}


void printAirPlaneTableOnly(void) {
    printTitle("비행기 편성표");

    printf(" ID   출발지          목적지          출발  도착   가격(원)   잔여석\n");
    printf("-------------------------------------------------------------------------------\n");

    for (int i = 0; i < 20; i++) {
        if (planeArr[i].fly_id == 0) continue;

        printf(" %-4d %-14s %-14s  %2d시  %2d시  %8d   %3d/56\n",
            planeArr[i].fly_id,
            planeArr[i].origin,
            planeArr[i].destination,
            planeArr[i].departure_time,
            planeArr[i].arrival_time,
            planeArr[i].cost,
            planeArr[i].seat_num
        );
    }

    printf("-------------------------------------------------------------------------------\n");
}



int findPlaneIndexByFlyId(int flyId) {
    for (int i = 0; i < 20; i++) {
        if (planeArr[i].fly_id == flyId) return i;
    }
    return -1;
}

int colFromChar(char seatCol) {
    if (seatCol >= 'a' && seatCol <= 'd') seatCol = seatCol - 'a' + 'A';
    if (seatCol == 'A') return 0;
    if (seatCol == 'B') return 1;
    if (seatCol == 'C') return 2;
    if (seatCol == 'D') return 3;
    return -1;
}

// planeArr의 "현재 상태"를 그대로 보여주기용(복사본 Plane p 출력 말고)
void printSeatMapFromPlaneIndex(int planeIndex) {
    Plane* p = &planeArr[planeIndex];

    printf("\n==================== 좌석 현황 ====================\n");
    printf("비행번호: %d | %s -> %s | %d시 ~ %d시 | %d원\n",
        p->fly_id, p->origin, p->destination, p->departure_time, p->arrival_time, p->cost);
    printf("잔여석: %d / 56\n", p->seat_num);
    printf("---------------------------------------------------\n");
    printf("      A    B    C    D\n");
    printf("    ---------------------\n");

    for (int r = 0; r < 14; r++) {
        printf("%2d | ", r + 1);
        for (int c = 0; c < 4; c++) {
            printf("%s    ", (p->seats[r][c] == 0) ? "□" : "■");
        }
        printf("\n");
    }

    printf("---------------------------------------------------\n");
    printf("표기: □(가능)  ■(예약)\n");
}

void reserve(void) {
    int flyId, planeIndex;
    int row;
    char seatColChar;
    int col;

    printf("\n[예약하기]\n");
    printAirPlaneTableOnly(); // 편성표 먼저 보여주고

    printf("예약할 비행번호 입력(취소 -1): ");
    scanf("%d", &flyId);
    if (flyId == -1) {
        selectPrint();
        return;
    }

    planeIndex = findPlaneIndexByFlyId(flyId);
    if (planeIndex == -1) {
        printf("존재하지 않는 비행번호입니다.\n");
        selectPrint();
        return;
    }

    if (planeArr[planeIndex].seat_num == 0) {
        printf("잔여석이 없습니다.\n");
        selectPrint();
        return;
    }

    // 좌석표 출력
    printSeatMapFromPlaneIndex(planeIndex);

    printf("\n좌석 선택 (예: 3 C)  => 3행 C열\n");
    printf("행(1~14) 입력: ");
    scanf("%d", &row);
    printf("열(A~D) 입력: ");
    scanf(" %c", &seatColChar);

    if (row < 1 || row > 14) {
        printf("행 입력이 잘못되었습니다.\n");
        selectPrint();
        return;
    }

    col = colFromChar(seatColChar);
    if (col == -1) {
        printf("열 입력이 잘못되었습니다.\n");
        selectPrint();
        return;
    }

    // 0-based
    int r = row - 1;
    int c = col;

    // 이미 예약 여부 체크
    if (planeArr[planeIndex].seats[r][c] == 1) {
        printf("이미 예약된 좌석입니다.\n");
        selectPrint();
        return;
    }

    // 예약 처리
    planeArr[planeIndex].seats[r][c] = 1;
    planeArr[planeIndex].seat_num--;

    // 예약 기록 저장
    bookCount++;
    bookArr[bookCount - 1].book_id = bookCount;
    bookArr[bookCount - 1].member_index = currentLoginIndex;
    bookArr[bookCount - 1].plane_index = planeIndex;
    bookArr[bookCount - 1].row = r;
    bookArr[bookCount - 1].col = c;

    printTitle("예약 완료");
    printf("예약번호: %d\n", bookArr[bookCount - 1].book_id);
    printf("회원: %s (%s)\n", memArr[currentLoginIndex].name, memArr[currentLoginIndex].memId);
    printf("비행번호: %d | %s -> %s\n", planeArr[planeIndex].fly_id, planeArr[planeIndex].origin, planeArr[planeIndex].destination);
    printf("좌석: %d%c\n", row, "ABCD"[c]);
    printf("가격: %d원\n", planeArr[planeIndex].cost);
    pauseEnter();
    selectPrint();
    return;
}

void showMyBookings(void) {
    printf("\n[내 예약내역]\n");
    printf("회원: %s\n", memArr[currentLoginIndex].name);
    printf("------------------------------------------------------------\n");

    int found = 0;
    for (int i = 0; i < bookCount; i++) {
        if (bookArr[i].member_index != currentLoginIndex) continue;

        found = 1;
        Plane* p = &planeArr[bookArr[i].plane_index];

        printf("예약번호:%d | 비행:%d | %s->%s | %d~%d | 좌석:%d%c | %d원\n",
            bookArr[i].book_id,
            p->fly_id,
            p->origin, p->destination,
            p->departure_time, p->arrival_time,
            bookArr[i].row + 1, "ABCD"[bookArr[i].col],
            p->cost);
    }

    if (!found) {
        printf("예약 내역이 없습니다.\n");
    }
    printf("------------------------------------------------------------\n");

    printf("돌아가려면 Enter: ");
    while (getchar() != '\n');
    getchar();

    selectPrint();
}


void initSeats(Plane* p) {
    int count = 0;
    for (int i = 0; i < 14; i++) {
        for (int j = 0; j < 4; j++) {
            p->seats[i][j] = 0; // 미예약
            count++;
        }
    }
    p->seat_num = count; // 잔여석(0의 개수)
}

void initialization(void) {
    // 회원 초기값
    memArr[0] = (Member){ "user123", "USER", "01012345678" };

    // 비행 편성 초기값 (fly_id는 너가 전부 1로 넣어놨길래 고유하게 1~11로 바꿔줌)
    planeArr[0] = (Plane){ 1,  "힘찬공항", "재영공항",  1,  5, 200000 };
    planeArr[1] = (Plane){ 2,  "보경공항", "영진공항",  2,  6, 400000 };
    planeArr[2] = (Plane){ 3,  "영진공항", "힘찬공항",  5,  7, 200000 };
    planeArr[3] = (Plane){ 4,  "보경공항", "재영공항",  8, 10, 100000 };
    planeArr[4] = (Plane){ 5,  "힘찬공항", "보경공항", 11, 17, 450000 };
    planeArr[5] = (Plane){ 6,  "힘찬공항", "영진공항", 13, 18, 200000 };
    planeArr[6] = (Plane){ 7,  "재영공항", "영진공항", 16, 19,  70000 };
    planeArr[7] = (Plane){ 8,  "힘찬공항", "재영공항", 18, 22,  65000 };
    planeArr[8] = (Plane){ 9,  "힘찬공항", "재영공항", 18, 20, 300000 };
    planeArr[9] = (Plane){ 10, "힘찬공항", "재영공항", 19, 23, 270000 };
    planeArr[10] = (Plane){ 11, "힘찬공항", "재영공항", 21, 22, 180000 };

    // 좌석(전부 0) + 잔여석(56) 초기화
    for (int i = 0; i < 11; i++) {
        initSeats(&planeArr[i]);
    }

    // 테스트
    planeArr[0].seats[0][0] = 1; planeArr[0].seat_num--;
    planeArr[0].seats[3][2] = 1; planeArr[0].seat_num--;
}

void printMember(Member m) {
    printf("%s / %s / %s\n", m.memId, m.name, m.phone_num);
}

void login(void) {
    char id[30];

    printf("로그인\n");
    printf("아이디 입력 : ");
    scanf("%29s", id);

    for (int i = 0; i < 10; i++) {
        if (memArr[i].memId[0] == '\0') continue;

        if (strcmp(memArr[i].memId, id) == 0) {
            currentLoginIndex = i;   // 로그인 상태 유지
            printf("로그인 성공\n");
            selectPrint();
            return;
        }
    }

    printf("없는 아이디 입니다.\n");
    start();
}

void addMember(void) {
    Member mem;

    printf("회원가입\n");

    printf("아이디 입력 : ");
    scanf("%29s", mem.memId);

    printf("이름 입력 : ");
    scanf("%29s", mem.name);

    printf("전화번호 입력 : ");
    scanf("%29s", mem.phone_num);

    for (int i = 0; i < 10; i++) {
        if (memArr[i].memId[0] == '\0') {
            memArr[i] = mem;
            printf("가입 완료 (index=%d)\n", i);
            printMember(memArr[i]);
            start();
            return;
        }
    }

    printf("회원이 가득 찼습니다.\n");
    start();
}

void printAirPlaneList(void) {
    int inputNum;

    printAirPlaneTableOnly();

    printf("\n좌석표 보기(돌아가기 -1) : ");
    if (scanf("%d", &inputNum) != 1) {
        clearLine();
        printf("숫자로 입력하세요.\n");
        pauseEnter();
        selectPrint();
        return;
    }

    if (inputNum == -1) {
        selectPrint();
    }
    else if (inputNum >= 1 && inputNum <= 11) {
        printSeats(inputNum - 1);
    }
    else {
        printf("잘못 입력하셨습니다.\n");
        pauseEnter();
        selectPrint();
    }
}


void logout(void) {
    currentLoginIndex = -1;
    printf("로그아웃 되었습니다.\n");
    start();
}

void selectPrint(void) {
    int selectNum;

    printTitle("메뉴");
    printf("현재 로그인: %s (%s)\n", memArr[currentLoginIndex].name, memArr[currentLoginIndex].memId);
    printDivider();

    printf("  1) 편성표 보기\n");
    printf("  2) 예약하기\n");
    printf("  3) 예약내역 확인\n");
    printf("  4) 로그아웃\n");
    printDivider();

    printf("선택: ");
    if (scanf("%d", &selectNum) != 1) {
        clearLine();
        printf("숫자로 입력하세요.\n");
        pauseEnter();
        selectPrint();
        return;
    }

    switch (selectNum) {
    case 1:
        printAirPlaneList();   // 이 함수 내부에서 돌아감 처리중이라 그대로
        return;
    case 2:
        reserve();
        return;
    case 3:
        showMyBookings();
        return;
    case 4:
        logout();
        return;
    default:
        printf("잘못된 입력입니다.\n");
        pauseEnter();
        selectPrint();
        return;
    }
}


void start(void) {
    int selectNum = 0;

    while (1) {
        printTitle("항공 예약 시스템");
        printf("  1) 로그인\n");
        printf("  2) 회원가입\n");
        printf("  3) 종료\n");
        printDivider();
        printf("선택: ");

        if (scanf("%d", &selectNum) != 1) {
            clearLine();
            printf("숫자로 입력하세요.\n");
            pauseEnter();
            continue;
        }

        switch (selectNum) {
        case 1:
            login();
            return;
        case 2:
            addMember();
            return;
        case 3:
            printf("\n프로그램을 종료합니다.\n");
            return;
        default:
            printf("잘못된 입력입니다.\n");
            pauseEnter();
            break;
        }
    }
}


void printSeats(int planeIndex) {
    Plane* p = &planeArr[planeIndex];

    printTitle("좌석 현황");
    printf("비행번호: %d | %s -> %s | %d시 ~ %d시 | %d원\n",
        p->fly_id, p->origin, p->destination, p->departure_time, p->arrival_time, p->cost);
    printf("잔여석: %d / 56\n", p->seat_num);
    printDivider();

    printf("        A     B   |   C     D\n");
    printf("      -------------------------\n");

    for (int r = 0; r < 14; r++) {
        printf(" %2d열 | ", r + 1);

        for (int c = 0; c < 4; c++) {
            printf("%s", (p->seats[r][c] == 0) ? "□" : "■");
            printf("     ");

            if (c == 1) printf("|   "); // 통로
        }
        printf("\n");
    }

    printDivider();
    printf("표기: □(예약 가능)  ■(예약 완료)\n");
    pauseEnter();
    selectPrint();
}
