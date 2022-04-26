#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE 80 /* The maximum length command */
#define HISTORY_SIZE 10

int main(void)
{
    char *args[MAX_LINE/2 + 1]; /* command line arguments */
    int should_run = 1; /* flag to determine when to exit program */
    
    char *history[HISTORY_SIZE];
    for (int i = 0; i < HISTORY_SIZE; i++)
        { history[i] = NULL; }
    int history_count = 0;
    int history_index = 0;
    int count = history_count % HISTORY_SIZE;
 
    while (should_run)
    {
        fflush(stdout);
        printf("osh>");
        char input[MAX_LINE];
        char history_buffer[MAX_LINE];
        char tokens[MAX_LINE];
        // scans string until "enter is pressed" and puts into input
        if (scanf(" %[^\n]", input) != 1)
            break;
        memcpy(tokens,input,MAX_LINE);
        memcpy(history_buffer,input,MAX_LINE);
        
        char *exclaim = strtok(tokens," ");
        char letter = exclaim[0];
        char exc = '!';
        int ex = exc;
        
        if (letter == ex) {
            char letter2 = exclaim[1];
            if (letter2 == ex) {
                if (history_count < 1) {
                    fprintf(stderr, "No History!\n");
                    continue;
                }
                else {
                    //replace !! with history could be an imporvement
                    memcpy(input,history[history_index],MAX_LINE);
                    printf("%s\n", input);
                    memcpy(history_buffer,input,MAX_LINE);
                }
            }
            else {
                int j = 1;
                char num[10];
                memset(&num[0],0,sizeof(num));
                do {
                    char letter2 = exclaim[j];
                    num[j-1] = letter2;
                    j++;
                } while (isdigit(exclaim[j]));
                int search = atoi(num);
                
                if ((search>history_count)
                    or (search<history_count-HISTORY_SIZE)
                    or (search < 1))
                {
                    fprintf(stderr, "History Not Availiable!\n");
                    continue;
                }
                else {
                    //replace !## with history could be an imporvement
                    memcpy(input,history[(search-1)%HISTORY_SIZE],MAX_LINE);
                    printf("%s\n", input);
                    memcpy(history_buffer,input,MAX_LINE);
                }  
             }
         }
  
         char *token = strtok(input, " ");
         int i = 0;
         bool bkgrd = false; //& concurrency check
         do {
            if (!strcmp(token,"&")) {
                bkgrd = true; 
                break;
            }
            args[i] = token;
            token = strtok(NULL, " ");
            i++;
        } while (token);
        args[i++] = NULL;

        history_count = history_count + 1;
        history_index = (history_count - 1) % HISTORY_SIZE; 
        free(history[history_index]);
        history[history_index] = strdup(history_buffer);
        
        if (!strcmp(*args,"exit")) { 
            should_run = 0;
            exit(0); 
        }

        if (!strcmp(*args,"history")) {
            int i = 0;
            do { if (history[history_index]) {
                    int id = (history_count-i-1) % HISTORY_SIZE; 
                    printf("%4d %s\n", history_count-i, history[id]);
                    i++; }
            } while ((i<HISTORY_SIZE) and (i<history_count));
            continue;
        }
        
        if (!strcmp(*args,"exit")) { 
            should_run = 0;
            exit(0); 
        }
        
        pid_t pid;
        pid = fork();
        if (pid < 0)
        {
            fprintf(stderr, "Fork Failed!\n");
            exit(1);
        }
        else if (pid == 0) 
        {
            // child process
            if (execvp(*args, args) < 0)
            {
                fprintf(stderr, "Execution Failed!\n");
                exit(1);
            }
                
        }
        else 
        {
            //parent process
            if (bkgrd)
                {
                    continue;
                }
            else wait(NULL);
        }
    }
    return 0;
}
