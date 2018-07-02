#include <stdio.h>

int main()
{
    int x;
    x = 5;
    int *ptr;
    ptr = &x;
    
    printf("%d\n",*ptr);
    printf("%d\n",x);
    printf("%d\n",ptr);
    printf("%d\n",&x);
}