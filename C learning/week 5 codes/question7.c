#include<stdio.h>
int main()
{
    float n;
    int leftmost3;
    printf("enter floating point number:");
    scanf("%f", &n);
    n=n*1000;
    leftmost3=(int)n%1000;
    printf("%d",leftmost3);
    return 0;
}
