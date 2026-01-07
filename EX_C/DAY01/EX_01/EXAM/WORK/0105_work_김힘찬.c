#include <stdio.h>                                                                   
#define STU 4  // 학생수                                                               
#define SUB 3  // 과목수    

void q5_12() {
	int score[STU + 1][SUB + 1] = {
		{ 100, 100, 100 },
		{  25,  20,  20 },
		{  35,  30,  30 },
		{  45,  40,  40 }
	};
	int i, j;
	int t_sum = 0;
	float a_sum = 0;

	printf("번호 국어 영어 수학 총점  평균\n");
	printf("===============================\n");

	for (i = 0; i < STU; i++) {
		printf(" %d   ", i + 1);

		for (j = 0; j < SUB; j++) {
			score[i][SUB] += score[i][j];
			score[STU][j] += score[i][j];
			printf("%3d  ", score[i][j]);
		}
		// 학생별 총점과 평균을 출력                                                
		printf(" %3d  %5.1f\n", score[i][SUB], score[i][SUB] / (float)SUB);
		t_sum += score[i][SUB];
		a_sum += score[i][SUB] / (float)SUB;
	}
	printf("===============================\n");
	printf("총점 ");
	
	for (j = 0; j < SUB; j++)
		printf("%3d  ", score[STU][j]);
	printf(" %3d  %5.1f\n", t_sum, a_sum / STU);
	puts("");
}

void q5_13() {
	int score[][STU + 1][SUB + 1] = {
		{ // 1반                                                                    
			{ 100, 100, 100 },  // 1반 1번                                      
			{  90,  90,  90 },  // 1반 2번                                      
			{  80,  80,  80 },  // 1반 3번                                      
			{  70,  70,  70 },  // 1반 4번                                      
		},

		{ // 2반                                                                    
			{  95,  95,  90 },  // 2반 1번                                      
			{  85,  85,  80 },  // 2반 2번                                      
			{  75,  75,  70 },  // 2반 3번                                      
			{  65,  65,  60 }   // 2반 4번                                      
		}
	};

	const int BAN = sizeof(score) / sizeof(score[0]);
	int i, j, k;

	for (i = 0; i < BAN; i++) {
		printf("[%d반]\n", i + 1);
		printf("번호 국어 영어 수학 총점  평균\n");
		printf("===============================\n");
		int t_sum = 0;
		float a_sum = 0;

		for (j = 0; j < STU; j++) {
			printf(" %d   ", j + 1);

			for (k = 0; k < SUB; k++) {
				score[i][j][SUB] += score[i][j][k];
				score[i][STU][k] += score[i][j][k];

				printf("%3d  ", score[i][j][k]);
			}
			// 학생별 총점과 평균을 출력                                              
			printf("%4d  %5.1f\n",
				score[i][j][SUB], score[i][j][SUB] / (float)SUB);
			t_sum += score[i][j][SUB];
			a_sum += score[i][j][SUB] / (float)SUB;
		}

		printf("===============================\n");
		printf("총점 ");

		for (k = 0; k < SUB; k++) {
			printf("%3d  ", score[i][STU][k]);
		}
		printf("%4d  %5.1f\n",
			t_sum, a_sum / STU);

		printf("\n\n");
	}
}

void q5_14() {
	char words[][2][10] = {
		{"chair","의자"},       // words[0][0], words[0][1]            
		{"computer","컴퓨터"},   // words[1][0], words[1][1]           
		{"integer","정수"}      // words[2][0], words[2][1]            
	};
	char answer[20];

	int i, cnt = 0;
	int len = sizeof(words) / sizeof(words[0]);

	const int WORD_CNT = sizeof(words) / sizeof(words[0]);

	for (i = 0; i < WORD_CNT; i++) {
		printf("Q%d. %s의 뜻은?", i + 1, words[i][0]);
		scanf("%s", answer);

		if (strcmp(words[i][1], answer) == 0) {
			printf("정답입니다.\n\n");
			cnt++;
		}
		else {
			printf("틀렸습니다. 정답은 %s입니다.\n\n", words[i][1]);
		}
	}
	printf("총 %d문제 중에 %d문제 맞추셨습니다.", len, cnt);
	printf("\n");

	return 0;
}

void main() {
	//q5_12();
	//q5_13();
	q5_14();
}