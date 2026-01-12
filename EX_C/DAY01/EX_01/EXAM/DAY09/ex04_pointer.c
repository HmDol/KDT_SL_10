#include<stdio.h>

void changeX(char* x) {
	x = "zzz";
}

int main(void) {
	char* x = "AAA";
	printf("x=%s\n", x);
	changeX(x);
	printf("x=%s\n", x);
}