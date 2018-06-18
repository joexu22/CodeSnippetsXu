#include <stdio.h>

/* understanding the input to output in c */

int main()
{
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);
}