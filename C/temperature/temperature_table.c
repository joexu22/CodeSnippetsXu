#include <stdio.h>

#define     LOWER   0       /* lower limit of table */
#define     UPPER   300     /* upper limit */
#define     STEP    20      /* step size */

/* print Fahrenheit-Celsius table
    for celsius = 300, 280, ..., 0 */

int main()
{
    /* header */
    printf("%10s %10s\n", "Fahrenheit", "Celsius");
    
    float fahr;
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%10.0f %10.1f\n", fahr, (5.0/9.0)*(fahr-32.0));
}