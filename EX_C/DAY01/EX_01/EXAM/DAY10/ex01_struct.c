#include<stdio.h>
#include<string.h>

// user define type
struct student {
	int no;
	char name[30];
	int kor, math, eng;
};
struct person {
	char name[30];
	int age;
	float height;
	float weight;
	char blood;
	char gender;
	
};

// 타입 재정의
typedef struct person Person;

int main(void) {
	struct student std1 = { 1, "Hong", 100, 90, 80 };
	struct student std2 = { 2, "Kim", 90, 70, 80 };

	Person kim = { 0 };
	Person park = { "박찬호", 10, 180.4, 76.3, 'A', 'M' };

	// 배열 선언과 동시에 초기화
	char msg1[10] = "Good";
	char msg2[] = { 'h', 'e', 'l', 'l', '0', '\0' };
	char msg3[10];

	for (int i = 0; i < 10; i++)
		msg3[i] = 'H';

	//속성변경
	park.age = 11;
	park.blood = '0';
	strcpy(park.name, "박혁거세");

	//속성확인
	printf("학번 : %d, 이름 : %s, 국어 : %d\n", std1.no, std1.name, std1.kor);
	printf("이름 : %s, 나이 : %d, 키 : %.1f, 몸무게 : %.1f, 혈액형 : %c\n",
		park.name, park.age, park.height, park.weight, park.blood);


	return 0;
}