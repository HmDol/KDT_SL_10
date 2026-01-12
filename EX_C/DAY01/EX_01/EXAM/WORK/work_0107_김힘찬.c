#include<stdio.h>
#include<string.h>

void q7_3();
void q7_5();
void q7_6();
void q7_7();
void q7_8();
void q7_9();
void q7_10();

int main(void) {
	q7_3();
	printf("\n");
	q7_5();
	printf("\n");
	q7_6();
	printf("\n");
	q7_7();
	printf("\n");
	q7_8();
	printf("\n");
	q7_9();
	printf("\n");
	q7_10();
	return 0;
}

void q7_3() {
	int arr[] = { 1,2,3,4,5,6 };
	int* ptr = &arr[0];

	//printf("ptr : %p / ptr+6 : %p", ptr, ptr+6); // 테스트용

	for (; ptr < arr + 6; ptr++)
		printf("%d ", *ptr);

	printf("\n");

}

void q7_5() {
	int arr[] = { 1,2,3,4 };
	printf("sizeof(arr) : %zu / sizeof(arr+0) : %zu\n", sizeof(arr), sizeof(arr + 0));
	// sizeof(arr) : int[4] 배열의 크기를 전달 -> 4*4 -> 16byte
	// sizeof(arr+0) : arr+0은 배열의 첫 원소를 가르키는 포인터 -> 64bit -> 8byte
}

void q7_6() {
	int arr[1][1] = { 5 };
	printf("&arr[0][0] : %p\n", &arr[0][0]);
	printf("&arr[0][0] : %d\n", *&arr[0][0]); // 테스트용 코드
	printf("*arr[0] : %d\n", *arr[0]); // arr[0]은 arr[0][0]의 첫번째 배열의 시작 원소의 주소값을 가지고 있음
									   // 따라서 *참조시 arr[0][0]의 첫배열의 첫원소를 참조하게 되어 5출력
	printf("*(int**)arr : %d", *(int**)arr);
}

void q7_7() {
	int arr[2][3] = { 1,2,3,4,5,6 };
	int(*ptr)[3] = arr;
	printf("%d\n", **ptr);
	ptr = (int(*)[3])0x100;
	printf("%p\n", ptr + 2);
	printf("%p\n", &ptr[1][2]);
	printf("%p\n", &ptr[2]);
	printf("%p\n", ptr[1] + 0);
}

void q7_8() {
	int(*ptr)[3][4] = (int(*)[3][4])0x100;
	printf("%p\n", *(ptr[0] + 1) + 2);
	printf("%d\n", sizeof(ptr[1]));
	printf("%d\n", sizeof(ptr + 1));
	printf("%p\n", &ptr[1]);
}

void q7_9() {
	char chArr[10];
	//char* ps = "ABC";
	int i = 0;
	// strcpy(chArr, ps);
	for (i = 0; ps[i]; i++) // ps[i]가 널이 아닌동안 반복
		chArr[i] = ps[i];

	chArr[i] = '\0'; //마지막에 널 삽입

	printf("chArr=%s\n", chArr);
	
}

void q7_10() {
	char* strArr[] = { "ABC","abc","123","2","aa","AAA","111","CCC","AAB" };
	const int LEN = sizeof(strArr) / sizeof(strArr[0]);
	int i, j;
	char* tmp;
	printf("[");
	for (i = 0; i < LEN; i++) {
		printf("%s,", strArr[i]);
	}
	printf("]\n");
	for (i = 0; i < LEN - 1; i++) {
		for (j = 0; j < LEN - i - 1; j++) {
			if (strcmp(strArr[j], strArr[j + 1]) > 0) {
				tmp = strArr[j];
				strArr[j] = strArr[j + 1];
				strArr[j + 1] = tmp;
			}
		}
	}
	printf("[");
	for (i = 0; i < LEN; i++) {
		printf("%s,", strArr[i]);
	}
	printf("]\n");

}


