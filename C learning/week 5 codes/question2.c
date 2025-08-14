#include<stdio.h>
#include<math.h>
int main()
{
    float a,b,c;
    printf("input sides of triangle:");
    scanf("%f%f%f",&a,&b,&c);
    if (a+b>c && b+c>a && c+a>b)
    {
        printf("triangle is valid\n");
        if (a==b && b==c && c==a)
            printf("triangle is equilateral\n");
        else if ((a==b && c!=a)||(b==c && a!=b))
            printf("triangle is isosceles\n");
        else
            printf("triangle is scalene\n"); 
    }
    else
        printf("these values dont form a triangle\n");
    //checking for right triangle
    if ((pow(a,2)==pow(b,2)+pow(c,2))||(pow(b,2)==pow(a,2)+pow(c,2))||(pow(c,2)==pow(b,2)+pow(a,2)))
        printf("triangle is a right angled triangle\n");
    return 0;
}
