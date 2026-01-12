// 함수와 포인터
#include<stdio.h>

void swapStr(char** a, char** b) {
	printf("함수 안쪽\n");
	char temp = *a;
	*a = *b;
	*b = temp;
	printf("함수끝\n");
}

void q8_5() {
	char* str1 = "ABC";
	char* str2 = "123";

	printf("str1 = %s, str2 = %s\n", str1, str2);

	swapStr(&str1, &str2);

	printf("str1 = %s, str2 = %s\n", str1, str2);
}

int main(void) {
	q8_5();
}