#include <stdio.h>

#define _CRT_SECURE_NO_WARNINGS
#define MIN  60                                                 
#define HOUR MIN*60        

void main() {
	//계산기
	int a, b;

	// 값 입력
	printf("a 값을 입력하세요: ");
	scanf("%d", &a);

	printf("b 값을 입력하세요: ");
	scanf("%d", &b);

	// 계산 결과 출력
	printf("%d + %d = %d\n", a, b, a + b);
	printf("%d - %d = %d\n", a, b, a - b);
	printf("%d * %d = %d\n", a, b, a * b);

	// 정수 나눗셈
	printf("%d / %d = %d\n", a, b, a / b);

	// 실수 나눗셈
	printf("%d / %d = %.2f\n", a, b, a / (float)b);

	// 3-6
	//int a = 10;
	//int b = 4;

	//printf("%d + %d = %d\n", a, b, a + b);
	//printf("%d - %d = %d\n", a, b, a - b);
	//printf("%d * %d = %d\n", a, b, a * b);
	//printf("%d / %d = %d\n", a, b, a / b);
	//printf("%d / %f = %f\n", a, (float)b, a / (float)b);
	
	// 3-7
	//int a = 10000000;
	//int b = 10000000;
	// 
	//long long c = a * c;
	//printf("c=%d\n", c);

	// 3-8
	//long long a = 1000000 * 1000000;
	//long long b = 1000000 * 1000000LL;

	//printf("a=%lld\n", a);
	//printf("b=%lld\n", b);
	
	// 3-9
	/*int a = 1000000;

	int result1 = a * a / a; 
	int result2 = a / a * a;

	printf("%d * %d / %d = %d\n", a, a, a, result1);
	printf("%d / %d * %d = %d\n", a, a, a, result2);*/

	// 3-10
	//char a = 'a';
	//char d = 'd';

	//char zero = '0';
	//char two = '2';

	//printf("'%c' - '%c' = %d\n", d, a, d - a);           // 'd'-'a'=3                 
	//printf("'%c' - '%c' = %d\n", two, zero, two - zero);  // '2'-'0'=2                
	//printf("'%c'=%d\n", a, a);
	//printf("'%c'=%d\n", d, d);
	//printf("'%c'=%d\n", zero, zero);
	//printf("'%c'=%d\n", two, two);

	// 3-11
	//int dayInSec = 24 * HOUR; // int dayInSec = 86400;      
	//int numOfDay = 10;
	//int result = dayInSec * numOfDay;

	//printf("%d day = %d sec\n", numOfDay, result);

	// 3-12
	//double pi = 3.141592;
	//double shortPi = (int)(pi * 1000) / 1000.0;

	//printf("%lf\n", shortPi);
	//printf("%5.3lf\n", shortPi);


	// 3-13
	//double pi = 3.141592;
	//double shortPi = (int)(pi * 1000 + 0.5) / 1000.0;

	//printf("%lf\n", shortPi);

	// 3-14
	//double pi = 3.141592;
	//double shortPi = (int)(pi*100 + 0.5) / 100.0;  

	//printf("%lf\n", shortPi);

	// 3-15
	//int x = 10, y = 8;

	//printf("%d을 %d로 나누면, \n", x, y);
	//printf("몫은 %d이고, 나머지는 %d입니다.\n", x / y, x % y);

	// 3-16
	/*int x = 10;
	int y = 8;

	printf("%3d %% %2d = %2d\n", x, y, x % y);
	printf("%3d %% %2d = %2d\n", x, -y, x % -y);
	printf("%3d %% %2d = %2d\n", -x, y, -x % y);
	printf("%3d %% %2d = %2d\n", -x, -y, -x % -y);*/



}