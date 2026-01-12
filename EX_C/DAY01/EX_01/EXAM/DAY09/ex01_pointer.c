#include<stdio.h>

int main(void) {
	int a;
	int* p;
	int** q;
	int*** r;

	a = 100;
	p = &a;
	q = &p;
	r = &q;

	printf("a : %3d\n", a);
	printf("*p : %3d\n", *p);
	printf("**q : %3d\n", **q);
	printf("***q : %3d\n", ***r);

	return 0;

}