#include<stdio.h>
int main(){
    int n,n1,n0,nextn;
    printf("enter n to print fibonacci series:");
    scanf("%d",&n);
    n0=0;
    n1=1;
    printf("%d %d ",n0,n1);
    for (;n1<n;){
        nextn=n0+n1;
        printf(" %d ",nextn);
        n0=n1;
        n1=nextn; 
    }
    return 0;
}