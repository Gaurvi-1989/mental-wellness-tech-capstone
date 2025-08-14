#include <stdio.h>
int main()
{
    int i, n, sum, a;
    printf("enter 5 digit integer:");
    scanf("%d", &n);
    if (n >= 10000 && n <= 99999)
    {
        for (i = 10; i <= 100000; i = i * 10)
        {
            a = n % i;
            a = a - n % (i / 10);
            a = a / (i / 10);
            sum = sum + a;
            printf("%d %d\n", a, sum);
        }
        printf("sum of digits is:%d", sum);
    }
    else
        printf("enter valid number");
    return 0;
}