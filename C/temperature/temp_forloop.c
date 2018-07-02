#include <stdio.h>

/* print Fahrenheit-Celsius table
    for celsius = 300, 280, ..., 0 */

int main()
{
    /* header */
    printf("%10s %10s\n", "Fahrenheit", "Celsius");
    
    float fahr;
    for (fahr = 300; fahr >= 0; fahr = fahr - 20)
        printf("%10.0f %10.1f\n", fahr, (5.0/9.0)*(fahr-32));
    return 0;
}
