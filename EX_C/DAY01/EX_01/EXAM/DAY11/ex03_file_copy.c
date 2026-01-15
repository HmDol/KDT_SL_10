# include<stdio.h>

int main(void) {
	char* fname1 = "./test.txt";
	char* fname2 = "./copy.txt";

	FILE* in_f = fopen(fname1, "r");
	FILE* out_f = fopen(fname2, "w");
	int ch = 0;

	if (!in_f || !out_f) {
		printf("파일%s을 열수 없음\n", !in_f ? fname1 : fname2);
		return 1;
	}

	printf("[%s]를 [%s]로 복제를 시작합니다. ", fname1, fname2);
	while ((ch = fgetc(in_f)) != EOF)
		fputc(ch, out_f);

	if (ferror(in_f) || ferror(out_f))
		printf("파일 복사 중 에러 발생");
	else
		printf("파일 복사 완료");

	fclose(in_f);
	fclose(out_f);
	return 0;

}