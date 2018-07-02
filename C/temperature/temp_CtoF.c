#include <stdio.h>

/* print Celsius-Fahrenheit table
    for celsius = 0, 20, ..., 200 */

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 200;
    step = 20;

    fahr = lower;
    
    /* headers for the column */
    printf("%10s %10s\n", "Celsius", "Fahrenheit");
    
    while (celsius <= upper) {
        fahr = (1.8 * celsius) + 32.0;
        printf("%10.0f %10.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
    return 0;
}