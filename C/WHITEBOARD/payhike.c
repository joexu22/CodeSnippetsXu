#include <stdio.h>
void salaryhike(int *var, int b)
{
    *var = *var + b;
}

int main()
{
    int salary = 0;
    int bonus = 0;
    printf("Enter current salary of employee: ");
    scanf("%d", &salary);
    printf("Enter bonus: ");
    scanf("%d", &bonus);
    salaryhike(&salary, bonus);
    printf("Final salary: %d", salary);
    return 0;
}