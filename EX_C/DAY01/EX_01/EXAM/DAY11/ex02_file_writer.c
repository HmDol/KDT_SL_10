#include<stdio.h>
#include<errno.h>

int main(void) {
	char* filename = "./test.txt";
	FILE* fp = fopen(filename, "r");


	if (fp == NULL) {
		printf("읽기모드로 파일 [%s] 열기에 실패했습니다.\n ", filename);
		printf("errno = %d\n", errno);
	}
	else {
		printf("읽기 모드로 파일 [%s] 열기에 성공했습니다.\n", filename);

	}
	fp = fopen(filename, "w");
	errno = 0;
	if (fp == NULL){
		printf("쓰기모드로 파일 [%s] 열기에 실패했습니다. \n", filename);
		printf("errno = %d\n", errno);
	}
	else {
		printf("쓰기 모드로 파일 [%s] 열기에 성공했습니다.\n", filename);

	}
	fclose(fp);
	printf("파일 [%s]를 닫습니다.", filename);

	return 0;
}