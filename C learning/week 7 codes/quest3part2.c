#include <stdio.h>
#include <math.h>
int main()
{
    int num, n1, n;
    printf("enter n to find armstron nums till n");
    scanf("%d", &n);
    for (num = 1; num < n; num++)
    {
        int sum=0;
        int num_dig = 0;
        int a = num;
        while (a > 0)
        {
            num_dig++;
            a = a / 10;
        }
        n1 = num;
        int s;
        while (n1 > 0)
        {
            s = n1 % 10;
            int i = 1;
            int pow = s;
            while (i < num_dig)
            {
                pow = pow * s;
                i++;
            }
            sum = sum + pow;
            n1 = n1 / 10;
        }
        if (sum == num)
            printf("\n%d is armstrong number", num);
    }
return 0;
}