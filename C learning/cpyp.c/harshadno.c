#include<stdio.h>
//number should be divisible by sum of digits
int main()
{
    printf("enter your number to check:\n");
    int n,sum=0,a,n1;
    scanf("%d",&n);
    n1=n;
    a=n%10;
    while(a>0){
        a=n1%10;
        sum+=a;
        n1/=10;
    }
    if (n%sum==0){
        printf("number is harshad number");
    }
    else printf("not harshad number");
    return 0;
}
