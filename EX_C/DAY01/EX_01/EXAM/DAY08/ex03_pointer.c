#include<stdio.h>

int main(void) {
	//변수 선언 및 초기화
	int value = 127;
	int* p = &value;

	printf("p	: 0x%p, %llu\n", p, (unsigned long long)p);
	p++;
	printf("p	: 0x%p, %llu\n", p, (unsigned long long)p);
	p++;
	printf("p	: 0x%p, %llu\n", p, (unsigned long long)p);


	p--;
	printf("p	: 0x%p, %llu\n", p, (unsigned long long)p);
	p--;
	printf("p	: 0x%p, %llu\n", p, (unsigned long long)p);


	return 0;
}