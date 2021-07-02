#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

//Structure that is passed into threads
struct Index{
    int *array1;
    int begin;
    int end;
    int *array2;
};

//sort function
//given an array, sorts the function using starting and ending index
//bubble sort within array
void sort(int a[], int start, int end)
{
    int i,j,tmp;
    for (i=start;i<(end-1);i++)
    {
        for (j=start;j<(end+start-i-1);j++)
        {
            if (a[j] > (a[j+1]))
            {
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    }
}

//sort thread function
void *sort_thread(void *indx)
{
    struct Index *index = indx;
    sort(index->array1, index->begin, index->end);
    return indx;
}

//merge function
void merge(int a[], int begin, int end, int b[])
{
    int i, j, k;
    i = begin;
    int mid = (begin + end)/2;
    j = mid;
    for (k = begin; k < end; k++)
    {
        if (i < mid && (j >= end || a[i] <= a[j]))
        {
            b[k] = a[i];
            i++;
        } else {
            b[k] = a[j];
            j++;
        }
    }
}

//merge thread function
void *merge_thread(void *indx)
{
    struct Index *index = indx;
    int *arrayA = index->array1;
    int *arrayB = index->array2;
    int begin = index->begin;
    int end = index->end;
    struct Index idx1 = {arrayA, begin, (begin+end)/2, arrayB};
    struct Index idx2 = {arrayA, (begin+end)/2, end, arrayB};

    pthread_t tid1,tid2;
    pthread_attr_t attr;

    pthread_attr_init(&attr);
    pthread_create(&tid1,&attr,sort_thread,&idx1);
    pthread_create(&tid2,&attr,sort_thread,&idx2);
    pthread_join(tid1,NULL);
    pthread_join(tid2,NULL);
    merge(index->array1, index->begin, index->end, index->array2);
    int i;
    for(i=0;i<index->end;i++)
        { printf("%d ", index->array2[i]); }
    printf("\n");
    return indx;
}

int main(int argc, char **argv)
{
    //basic error checking
    if (argc != 2) {
    fprintf(stderr,"usage: a.out <filename>\n");
    return -1;
    }

    //count number of inputs
    int tmp, count=0;
    FILE *myFile;
    myFile = fopen(argv[1],"r");
    do { if (fscanf(myFile, "%d", &tmp) == 1) {
            count++;
         }
    } while (!feof(myFile));
    fclose(myFile);
    
    //initilize arrays
    int arrayA[count];
    int arrayB[count];
    count = 0;
    myFile = fopen(argv[1],"r");
    do { if (fscanf(myFile, "%d", &arrayA[count]) == 1)
            {
                count++;
            }
    } while (!feof(myFile));
    fclose(myFile);

    //structure to pass into index
    struct Index idx = {arrayA, 0, count, arrayB};

    //create threads
    pthread_t tid;
    pthread_attr_t attr;

    pthread_attr_init(&attr);
    pthread_create(&tid,&attr,merge_thread,&idx);
    pthread_join(tid,NULL);

    return 0;
}
