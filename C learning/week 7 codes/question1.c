#include <stdio.h>
int main()
{
    int n, k, count, sum = 0;
    printf("enter n to find sum of prime numbers till n:");
    scanf("%d", &n);
    for (k = 2; k <= n; k++)
    {
        count = 0;
        int i = 1;
        while (i <= k)
        {
            if (k % i == 0)
                count++;
            i++;
        }
        if (count == 2)
        {
            sum += k;
        }
    }
    printf("sum of prime numbers till %d is %d", n, sum);
    return 0;
}
