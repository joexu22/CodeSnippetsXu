#include <stdio.h>
int main()
{
    unsigned int i = 1;
    char *c = (char *)&i;
    if (*c)
    {
        printf("Little Endian");
    }
    else
    {
        printf("Big Endian");
    }
    getchar();
    return 0;
}