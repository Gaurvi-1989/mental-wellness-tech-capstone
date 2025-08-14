#include<stdio.h>
int main(){
    int count=0,l=500,p,d=100,n=-50;
    while(p<l){
        p+=d+n;
        count++;
        printf("progress of snail on day %d is %d\n",count,p);
        if (p==l) break;
    }
    printf("days taken by snail is %d",count);

    return 0;
}