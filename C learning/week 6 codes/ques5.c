#include <stdio.h>
// #include <math.h>
int main()
{
    printf("enter number :");
    int count = 0;
    float n;
    scanf("%f", &n);
    while (n > 1)
    {
        n = n / 2.0;
        if (n == 1.000000)
        {
            count++;
            break;
        }
    }
    if (count == 1)
        printf("number is power of 2");
    else
        printf("number is not a power of 2");
    return 0;
}
// int main()
// //convert lowercase to uppercase
// {
//     char c;
//     printf("enter lowercase:");
//     if ((int)c<=122&&(int)c>=97){

//     }
//     else
//         printf("enter lowercase alphabet");
//     return 0;
// }
