#include <stdio.h>
int main()
{
    printf("enter age:");
    int age;
    scanf("%d", &age);
    if (age >= 18 && age <= 21)
        printf("\nage is from 18 to 21");
    else
        printf("\nage is not from 18 to 21");

    printf("\nenter length");
    float length;
    scanf("%f", &length);
    if (length > 0.1 && length < 1.5)
        printf("\nlength is greater than 0.1 and less than 1.5");
    else
        printf("\nlength is not greater than 0.1 or not less than 1.5");

    printf("\nenter year: ");
    int year;
    scanf("%d", &year);
    if (year % 4 == 0)
        printf("\nyear is divisible by 4");
    else
        printf("\nyear is not divisible by 4");

    printf("\nenter x,y and z:");
    int x, y, z;
    scanf("%d%d%d", &x, &y, &z);
    if ((y > x) && (y < z))
        printf("\ny is greater than x and less than z");
    else
        printf("\ny is not greater than x or not less than z");

    printf("\nenter w:");
    int w;
    scanf("%d", &w);
    if ((w == 6) || (w <= 3))
        printf("w is either equal to 6 or not greater than 3");
    else
        printf("w is neither not equal to 6 nor greater than 3");
    return 0;
}