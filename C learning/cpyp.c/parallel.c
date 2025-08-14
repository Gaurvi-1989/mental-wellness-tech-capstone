#include<stdio.h>
int main(){
    float x1,y1,x2,y2;
    float a1,b1,a2,b2;
    printf("enter coordinates\n");
    scanf("%f%f%f%f",&x1,&y1,&x2,&y2);
    printf("enter coordinates\n");
    scanf("%f%f%f%f",&a1,&b1,&a2,&b2);
    float m1,m2;
    m1=(y2-y1)/(x2-x1);
    m2=(b2-b1)/(a2-a1);
    if (m1==m2) printf("parallel");
    return 0;
}