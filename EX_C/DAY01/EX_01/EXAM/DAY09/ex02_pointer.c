#include<stdio.h>

// 배열 포인터, 즉 포인터를 저장하는배열

int main(void) {
	// 다양한 배열 : 동일한 타입!!
	int num[] = { 10, 20, 30 };
	int n1 = 100, n2 = 200, n3 = 300;
	int* pArr[3];

	// 배열 초기화
	pArr[0] = &n1;
	pArr[1] = &n2;
	pArr[2] = &n3;

	// 배열 요소 읽기
	for (int i = 0; i < 3; i++) {
		printf("[%d] - %p, %d\n", i, pArr[i], *pArr[i]);
	}

	return 0;
}