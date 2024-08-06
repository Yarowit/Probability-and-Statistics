#include <time.h>
#include <stdlib.h>
#include <stdio.h>


int main(){
    srand(time(NULL));
    FILE *fptr;
    fptr = fopen("cnums.txt","w");

    for(int i = 0; i < 1000; i++)
        fprintf(fptr,"%d",rand()%2);
    fclose(fptr);   

}
