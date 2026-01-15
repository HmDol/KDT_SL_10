#include <stdio.h>
#include <string.h>

// ======================= 함수 선언 (프로토타입) =======================
void start(void);
void login(void);
void addMember(void);
void selectPrint(void);
void printMember(Member);
void printAirPlaneList(void);
void initialization(void);



// ----------------------- 구조체 -----------------------------------
typedef struct member {
    char memId[30];         // 아이디
    char name[30];          // 이름
    char phone_num[30];     // 전화번호
} Member;

typedef struct airplan {
    int fly_id;             // 비행번호
    char origin[30];        // 출발지
    char destination[30];   // 목적지
    int departure_time;     // 출발시간
    int arrival_time;       // 도착시간
    int cost;               // 가격
}Plane;

// ---------------------- 전역 변수 ---------------------------------
Member memArr[10] = { 0 };
Plane planeArr[20] = { 0 };


int currentLoginIndex = -1;

// ======================= 함수 정의 =======================

void login() {
    char id[30];

    printf("로그인 입장\n");
    printf("아이디 입력 : ");
    scanf("%29s", id);

    for (int i = 0; i < 10; i++) {
        if (memArr[i].memId[0] == '\0') continue;

        if (strcmp(memArr[i].memId, id) == 0) {
            currentLoginIndex = i;   // 로그인 상태 유지를 위한 
            printf("로그인 성공\n");
            selectPrint();
            return;
        }
    }

    printf("없는 아이디 입니다.\n");
    start();
}

void printAirPlaneList() {
    printf("-------------비행기 편성표--------------");
    


    printf("-----------------------------------------");



}

void selectPrint() {
    int selectNum;
    printf("selectPrint 입장\n");
    printf("현재 로그인한 회원 정보\n");
    printMember(memArr[currentLoginIndex]);
    printf("1.편성표보기 / 2.예약하기 / 3. 예약내역 확인 / 4. 로그아웃\n");
    printf("선택 : ");
    scanf("%d", &selectNum);

    switch (selectNum) {
    case 1:
        printAirPlaneList();
        break;
    case 2:
        break;
    case 3:
        break;

    case 4:
        break;

    default:
        break;


    }

}

void printMember(Member m) {
    printf("%s / %s / %s\n", m.memId, m.name, m.phone_num);
}

void addMember() {
    Member mem;

    printf("회원가입 입장\n");

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
            break;
        }
    }

    start();
}

void initialization(void) {
    Member m1 = { "user", "유저", "01012341234" };
    memArr[0] = m1;

}


void start() {
    int selectNum = 0;

    while (1) {
        printf("1. 로그인\t2. 회원가입\n");
        printf("선택: ");

        if (scanf("%d", &selectNum) != 1) {
            while (getchar() != '\n');
            printf("숫자로 입력하세요.\n");
            continue;
        }

        switch (selectNum) {
        case 1:
            login();
            return;
        case 2:
            addMember();
            return;
        default:
            printf("잘못된 입력입니다.\n");
            break;
        }
    }
}

int main(void) {   
    initialization();
    start();
    return 0;
}
