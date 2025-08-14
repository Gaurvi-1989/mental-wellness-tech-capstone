#include<stdio.h>
int main(){
    int a=6;
    int b=9;
    int c=14;
    int f=1;
    c=a+b||f;
    printf("1) %d\n",c);
    printf("2) %d\n",a!=7&&a%2==0);
    printf("3) %d\n",!(b>=12)&&a%2==0);
    printf("4) %d",!(a>5||c<a+b));
    return 0;
}