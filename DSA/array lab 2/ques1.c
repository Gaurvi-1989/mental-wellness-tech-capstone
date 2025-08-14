#include<stdio.h>
// int main(){
//     int a,b;
//     printf("enter a and b  ");
//     scanf("%d",&a);
//     scanf("%d",&b);
//     a=a+b;
//     b=a-b;
//     a=a-b;
//     printf("a=%d and b=%d",a,b);
// }
int main(){
    int *a,*b;
    int x,y;
    a=&x;
    b=&y;
    printf("enter x and y  ");
    scanf("%d",&x);
    scanf("%d",&y);
    int temp=*a;
    x=*b;
    y=temp;
    printf("x=%d and y=%d",x,y);
}
