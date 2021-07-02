#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>

int collatz(long long num)
{
    if (num <= 0)
    {
        fprintf(stderr, "Number must be positive! Exiting...\n");
        exit(1);
    }
    else
    {
        while (num != 1)
        {
            printf("%lld,", num);
            if (num % 2 == 0)
            {
                num = num / 2;
            }
            else
            {
                num = 3 * num + 1;
            }
        }
        printf("%lld\n", num);
        exit(0);
    }
}

int main()
{
    long long number;
    printf("Enter a positive number: ");
    
    scanf("%lld", &number);
    
    pid_t pid;
    pid = fork();
    if (pid < 0)
    {
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if (pid == 0) 
    {
        // child process
        collatz(number);
    }
    else 
    {
        //parent process
        wait(NULL);
    }
    return 0;
}
