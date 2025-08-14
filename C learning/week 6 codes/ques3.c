#include <stdio.h>
int main()
{
    printf("enter marks to get feedback");
    int m;
    scanf("%d", &m);
    int a;
    a = (m - m % 10) / 10;
    switch (a)
    {
    case 9:
    case 8:
        printf("marks from 80 to 99 are excellent");
        break;
    case 7:
        printf("marks from 70 to 79 are good");
        break;
    case 6:
        printf("marks from 60 to 69 are average");
        break;
    case 5:
    case 4:
        printf("marks from 40 to 59 are below average");
        break;
    case 3:
    case 2:
    case 1:
    case 0:
        printf("marks below 40 are fail");
        break;
    default:
        printf("enter valid marks");
    }
    return 0;
}