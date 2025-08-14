#include<stdio.h>
int main(){
    typedef  struct {
    char name[20];
    int roll;
    int marks[6];
} student;
student arr[5];
for(int i=0;i<5;i++){
    printf("enter name of student: ");
    scanf("%s",&arr[i].name);
    printf("enter roll no. of student: ");
    scanf("%d",&arr[i].roll);
    printf("enter marks of 6 subjects ");
    for(int j=0;j<6;j++){
        scanf("%d",&arr[i].marks[j]);
    }
}
for(int i=0;i<5;i++){
    // printf("name of student: ");
    printf("%s ",arr[i].name);
    // printf(" roll no. of student: ");
    printf("%d ",arr[i].roll);
    // printf("marks of 6 subjects ");
    for(int j=0;j<6;j++){
        printf("%d ",arr[i].marks[j]);
    }
}
}