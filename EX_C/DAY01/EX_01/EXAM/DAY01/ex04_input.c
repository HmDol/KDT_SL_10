/********************************************************************
* filename : ex03_input.c
* Description : 표준 입력


* Note : 문자 1개, 문자 여러개
*********************************************************************/
#pragma warning(disable:4996)
# include <stdio.h>

int main(void) {


	// 입력데이터 저장용 변수 : 지역변수
	char ch=0;		// 문자 1개 저장 변수
	char name[10];	// 문자 여러개 저장 변수

	// 변수 저장 데이터 출력하기
	printf("ch에 저장된	  데이터 : %c\n", ch);
	printf("name에 저장된 데이터 : %p\n", name);

	//키보드로 입력 받은 데잍 ㅓ저장 및 확인
	printf("'학점과 이름 입력'");
	scanf("%c %s", &ch, name);

	printf("학점 %c, 이름 %s", ch, name);


}