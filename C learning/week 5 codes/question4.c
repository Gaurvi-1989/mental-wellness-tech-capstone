#include<stdio.h>
int main()
{
    int age;
    printf("enter age:");
    scanf("%d",&age);
    if (age>=60)
        printf("you are considered for retirement");
    else if(age>0 && age<60)
        printf("you can continue working");
    else
        printf("enter a valid age");
    return 0;
}
