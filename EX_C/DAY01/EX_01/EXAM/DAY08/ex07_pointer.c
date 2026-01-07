#include<stdio.h>

int main(void) {
	const int MAX = 100;
	int		 value = 10;

	int* p1 = &value;

	//현재값
	printf("*p1 = %d, value = %d\n", *p1, value);

	//변경
	*p1 = 7;
	printf("*p1 = %d, value = %d\n", *p1, value);

	return 0;
}