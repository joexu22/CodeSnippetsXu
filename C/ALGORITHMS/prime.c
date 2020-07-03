#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int find_divisor(int n, int divisor) {
	if ((divisor * divisor) > n) {
		return n;
	} else if ((n % divisor) == 0) {
		return divisor;
	} else {
		return find_divisor(n, divisor+1);
	}
}

int smallest_divisor(int n) {
	return find_divisor(n, 2);
}

int prime(int n) {
	return (smallest_divisor(n) == n);
}

int main()
{
	printf("%s\n", prime(1) ? "true" : "false");
	printf("%s\n", prime(2) ? "true" : "false");
	printf("%s\n", prime(3) ? "true" : "false");
	printf("%s\n", prime(4) ? "true" : "false");
	printf("%s\n", prime(5) ? "true" : "false");
	printf("%s\n", prime(6) ? "true" : "false");
	printf("%s\n", prime(7) ? "true" : "false");
	printf("%s\n", prime(8) ? "true" : "false");
	printf("%s\n", prime(9) ? "true" : "false");
	printf("%s\n", prime(10) ? "true" : "false");

	return 0;
}