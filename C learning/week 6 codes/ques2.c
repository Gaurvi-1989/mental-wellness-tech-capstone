#include <stdio.h>
int main(){
    printf("enter number to classify in even or odd  ");
    int n;
    scanf("%d",&n);
    switch(n%2){
        case 0: printf("number is even"); break;
        case 1: printf("number is odd"); break;
    }
    return 0;
}