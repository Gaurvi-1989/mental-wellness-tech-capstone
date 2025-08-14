//q1
#include<stdio.h>
int main()
{
    int unit;
    float bill;
    printf("enter electricity units to calculate bill:");
    scanf("%d",&unit);
    if (unit<=50)
        bill=unit*0.5;
    else if (unit<=150)
    { 
        unit=unit-50;
        bill=50*0.5+unit*0.75;
    }
    else if (unit<=250)
    {
        unit=unit-150;
        bill=50*0.5+100*0.75+unit*1.2;
    }
    else {
        unit=unit-250;
        bill=50*0.5+100*0.75+100*1.2+unit*1.5;
    }
    printf("the bill amount will be %f",bill);
    return 0;
}
