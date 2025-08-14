// part1
#include <stdio.h>
#include <math.h>
int main()
{
    int n, n1, sum = 0;
    printf("enter n");
    scanf("%d", &n);
    int num_dig = 0;
    int a = n;
    while (a > 0)
    {
        num_dig++;
        a = a / 10;
    }
    n1 = n;
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
    if (sum == n)
        printf("\nnumber is armstrong number");
    else
        printf("number is not armstrong number");
    return 0;
}