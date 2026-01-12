#include<stdio.h>

typedef struct student {
	int no;
	char name[10];
	int kor, math, eng;
} Student;

int main(void) {
	Student stuArr[] = {
		{1, "kim", 100, 100, 100},
		{1, "lee", 91, 92, 93},
		{1, "choi", 81, 82, 83},
		{1, "park", 71, 72, 73}
	};
	const int Len = sizeof(stuArr) / sizeof(stuArr[0]);
	int total, i;
	float average;

	printf("sizeof(stuArr)		=%zu\n", sizeof(stuArr));
	printf("sizeof(stuArr[0])		=%zu\n", sizeof(stuArr[0]));
	printf("sizeof(Student)		=%zu\n", sizeof(Student));
	printf("sizeof(struct student)		=%zu\n", sizeof(struct student));
	printf("Len = %d\n", Len);

	printf("\n번호 이름      국어 수학 영어 총점 평균\n");
	printf("==========================================\n");
	for (i = 0; i < Len; i++) {
		total = stuArr[i].kor + stuArr[i].math + stuArr[i].eng;
		average = total / (float)3;

		printf("%4d  %-10s %4d %4d %4d %4d %6.2f\n", stuArr[i].no,
			stuArr[i].name, stuArr[i].kor, stuArr[i].math, stuArr[i].eng, total, average);
	}
}