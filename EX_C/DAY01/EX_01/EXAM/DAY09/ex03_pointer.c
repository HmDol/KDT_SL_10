#include<stdio.h>

int main(void) {
	char* strings[3] = {
		"how are you?",
		"hello world",
		"c language programming"
	};

	for (int i = 0; i < 3; i++) {
		printf("%s\n", strings[i]);
	}

	return 0;
}