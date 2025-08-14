#include <stdio.h>
int main()
{
    float n;
    int last2digit;
    printf("enter floating point number:");
    scanf("%f", &n);
    last2digit=(int)n%100;
    printf("last 2 digits are %d", last2digit);
    return 0;
}
