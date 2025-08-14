#include<stdio.h>
int main()
{
    int qty,price,dis=0;
    printf("enter qty and price");
    scanf("%d%d",&qty,&price);
    float bill;
    if (qty>1000)
        bill=qty*price*0.9;
    else 
        bill=qty*price;
    printf("the bill is %f",bill);
    return 0;
}
