#include <stdio.h>
#include <stdbool.h>

int prime(int n) {
	return n;
}

void printNumber(int number) {
	printf("%d\n", number);
}

void printCharacter(char *s) {
	printf("%c\n", *s);
}

void myFunction(void (*f) (int)) {
	for (int i = 0; i < 5; i++) {
		(*f) (i);
	}
}

void printHelloWorld() {
	printf("Hello World!\n");
}

void printHelloWorldFunction(void (*f) ()){
	f();
}

void striter(char *s, void (*f) (char *)) {
	if (s) {
		for (int i = 0; s[i]; i++) {
			f(&s[i]);
		}
	}
	return;
}

int main()
{
	printf("hello, world\n");

	char str[8];
	printNumber(7);

	// printf(prime());
    bool valueTrue = true;
	bool valueFalse = false;
	printf("%s\n", valueTrue ? "true" : "false");
	printf("%s\n", valueFalse ? "true" : "false");

	myFunction(printNumber);
	printHelloWorldFunction(printHelloWorld);

	striter("abc", printCharacter);

	return 0;
}