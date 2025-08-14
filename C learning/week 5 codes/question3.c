#include <stdio.h>
int main()
{
    int n, i,count;
    printf("enter number:");
    scanf("%d", &n);
    if (n % 2 == 0)
        printf("number is even ");
    else
        printf("number is odd ");
    for (i = 2; i <= n / 2; i++)
    {
        if (n % i == 0)
            count=count+1;
    }
    if (count==0){
        printf("and prime");
    }
    else
         printf("and not prime");
    return 0;
}
