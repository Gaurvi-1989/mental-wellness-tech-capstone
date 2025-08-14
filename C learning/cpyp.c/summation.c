#include<stdio.h>
int main(){
    printf("enter n:");
    int n;
    float k;
    float i,sum=0;
    scanf("%d",&n);
    for(k=1;k<=n;k++){
        i=(2*k-1)/k;
        sum+=i;
    }
    printf("the summation is %f",sum);
    return 0;
}