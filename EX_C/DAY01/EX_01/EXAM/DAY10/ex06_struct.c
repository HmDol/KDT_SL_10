#include<stdio.h>

typedef struct student {
	int no;
	int kor, math, eng;
} Student;

// 사용자 정의 함수
// ----------------------------------------------------------------------------
// 함수 기능 : 구조체 속성/필드 출력 기능
// 함수 이름 : printAttr
// 매개 변수 : Student std
// 반환 결과 : 없음
// ----------------------------------------------------------------------------
void printAttr(Student std) {
	printf("%d, %d, %d, %d\n", std.no, std.kor, std.eng, std.math);


}

// ----------------------------------------------------------------------------
// 함수 기능 : 구조체 속성/필드 출력 기능
// 함수 이름 : printField
// 매개 변수 : Student* ptr
// 반환 결과 : 없음
// ----------------------------------------------------------------------------
void printField(const Student* const ptr) {
	printf("%d, %d, %d, %d\n", ptr->no, ptr->kor, ptr->eng, ptr->math);
	Student ss = { 0 };
	// ptr = &ss;
	 
	//ptr->math = 77;
	//ptr->kor = 92;


}


int main(void) {
	Student st1 = { 1, 100, 100 ,100 };
	Student* pst = &st1;

	Student st2 = st1;
	
	// call by value
	printAttr(st1);
	printf("%d, %d, %d, %d\n", st1.no, st1.kor, st1.eng, st1.math);
	// call by reference
	printField(&st1);
	printf("%d, %d, %d, %d\n", st1.no, st1.kor, st1.eng, st1.math);


	return 0;
}