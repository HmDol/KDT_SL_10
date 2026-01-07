#include<stdio.h>

long long factorial(int n) {
	if (n <= 0 || n > 20) return -1;
	if (n <= 1) return 1;

	return n * factorial(n - 1);
}

int main(void) {
	int i = 0, n;
	printf("숫자를 입력해주세요 : ");
	if (scanf("%d", &n) != 1) { printf("유효하지 않은 입력"); return 0; }
	long long result = 0;

	for (i = 1; i <= n; i++) {
		result = factorial(i);
		if (result == -1) { printf("유효하지 않은 값입니다. %d", n); break; }

		printf("%2d!=%20lld\n", i, result);
	}
	return 0;
}