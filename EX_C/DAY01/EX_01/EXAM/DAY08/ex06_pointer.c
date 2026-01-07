#include<stdio.h>

// user define function
void printValue(int , int );
void changeValue(int*, int*);
int main(void) {
	int a = 7, b = 8;

	//함수 호출 -> call by value
	printValue(a, b);
	printf("[main] a=%d, b=%d\n", a, b);


	changeValue(&a, &b);
	printf("[main] a=%d, b=%d\n", a, b);
}

void printValue(int a, int b) {
	a += 10;
	b *= a;
	printf("a=%d, b=%d\n", a, b);
}

void changeValue(int* a, int* b) {
	*a += 10; // *a = *a + 10;
	*b *= *a; // *b = *b * *a;
}