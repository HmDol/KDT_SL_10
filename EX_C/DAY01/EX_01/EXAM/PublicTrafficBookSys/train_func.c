#include "train_header.h"
Customer customers[MAXCUSTOMER];
int Ccount = 0;

Train trains[MAXTRAIN] = {
	{101, "09:00", "동대구", "동탄", {0}},
	{102, "10:00", "동대구", "부산", {0}},
	{103, "11:00", "동대구", "동탄", {0}},
	{104, "12:00", "동대구", "부산", {0}}
};

void trainStart() {
	int select;
	Customer* userinfo = NULL;

	while (1)
	{
		//로그인
		printf("===================================================\n");
		printf("|                                                 |\n");
		printf("|                    SRT예약                      |\n");
		printf("|                                                 |\n");
		printf("===================================================\n");
		printf("|  1. 회원가입                                    |\n");
		printf("|  2. 로그인                                      |\n");
		printf("|  3. 종료                                        |\n");
		printf("===================================================\n");
		printf("메뉴 선택 --> ");
		scanf("%d", &select);

		switch (select)
		{
		case 1:
			signup();
			break;
		case 2:
			userinfo = trainlogin();
			int ret;
			char* end;
			while (1)
			{
				printf("===================================================\n");
				printf("|  도착지를 선택해주세요.                         |\n");
				printf("===================================================\n");
				printf("|  1 - 동탄                                       |\n");
				printf("|  2 - 부산                                       |\n");
				printf("===================================================\n");
				printf("--> ");
				scanf("%d", &ret);

				if (ret == 1)
				{
					end = "동탄";
					break;
				}
				else if (ret == 2)
				{
					end = "부산";
					break;
				}
				else
					printf("잘못된 선택입니다.\n");
			}

			train(end);
			break;
		case 3:
			return 0;
		default:
			printf("잘못된 선택입니다.\n");
		}
	}
	return 0;
}

void signup(void)
{
	if (Ccount >= MAXCUSTOMER)
	{
		printf("회원 최대치 도달!\n");
		return;
	}
	int ID;
	Customer* c = &customers[Ccount];

	while (1)
	{
		int check = 0;
		printf("아이디 입력 ex)123 : ");
		scanf("%d", &ID);
		for (int i = 0; i < Ccount; i++)
		{
			if (ID == customers[i].id)
			{
				printf("이미 존재하는 아이디 입니다. 다시 입력하세요.\n");
				check = 1;
				break;
			}
		}
		if (check == 0)
		{
			c->id = ID;
			break;
		}
	}
	printf("비밀번호 입력 ex)1234 : ");
	scanf("%d", &c->pw);
	printf("이름 입력 ex)영어 이니셜 cyj: ");
	scanf(" %4s", c->name);
	printf("전화번호 입력 ex) 010-3922-7473 : ");
	scanf(" %13s", c->phone);

	Ccount++;
	printf("회원가입 완료 - %s\n", c->name);
}

Customer* trainlogin(void)
{
	int id, pw;
	while (1)
	{
		printf("ID : ");
		scanf("%d", &id);
		printf("PW : ");
		scanf("%d", &pw);

		for (int i = 0; i < Ccount; i++)
		{
			if (customers[i].id == id && customers[i].pw == pw)
			{
				printf("로그인 성공 - %d\n", customers[i].id);
				return &customers[i];
			}
		}
		printf("ID 또는 PW가 틀렸씁니다. 다시 입력하세요.\n");
	}
}
void train(const char* end)
{
	const char* start = "동대구";
	trainlist(end);
}

void trainlist(const char* end)
{
	int count = 0;
	int pick;
	int idxList[MAXTRAIN];

	printf("===================================================\n");
	printf("|  [동대구] -> [%s] 기차 목록                   |\n", end);
	printf("===================================================\n");

	for (int i = 0; i < MAXTRAIN; i++)
	{
		if (strcmp(trains[i].end, end) == 0)
		{
			printf("%d. %s (열차번호 %d)\n", count + 1, trains[i].t_time, trains[i].t_num);

			idxList[count] = i;
			count++;
		}
	}
	printf("===================================================\n");
	printf("시간 선택 : ");
	scanf("%d", &pick);

	if (pick<1 || pick>count)
	{
		printf("잘못된 선택입니다.\n");
		return NULL;
	}

	Train* selected = &trains[idxList[pick - 1]];
	trainseat(selected);
}

void trainseat(Train* t)
{
	int seat;
	int rows = SEATNUM / 4;

	while (1)
	{
		int seatNum = 1;
		printf("===================================================\n");
		printf("|  [동대구] -> [%s] %s 열차 좌석 정보        |\n", t->end, t->t_time);
		printf("===================================================\n");



		for (int i = 0; i < rows; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				printf("[%2d:%c] ", seatNum, t->seat[seatNum - 1] ? 'X' : 'O');
				seatNum++;
			}
			printf("\n");
		}


		printf("예약할 좌석 번호 선택 : ");
		scanf("%d", &seat);

		if (seat < 1 || seat > SEATNUM)
		{
			printf("잘못된 좌석 번호입니다.\n");
			continue;
		}



		if (t->seat[seat - 1] == 1)
		{
			printf("이미 예약된 좌석입니다.\n");
			continue;
		}
		break;
	}
	t->seat[seat - 1] = 1;
	printf("예약 완료! %s 열차 %d번 좌석\n자동로그아웃, 초기화면으로 돌아갑니다.\n", t->t_time, seat);
}