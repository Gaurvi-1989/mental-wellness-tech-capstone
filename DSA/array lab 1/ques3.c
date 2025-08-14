#include<stdio.h>
int main(){
    int n1,m1,n2,m2;
    printf("enter values of n and m(dimensions) for the 2 arrays:");
    scanf("%d",&n1);
    scanf("%d",&m1);
    scanf("%d",&n2);
    scanf("%d",&m2);
    int i,j;
    int arr1[n1][m1];
    int arr2[n2][m2];
    if(n1!=n2 | m1!=m2){
        printf("cannot be added because dimensions are not same");
    }
    else{
    printf("enter the values in array 1\n");
    for(i=0;i<n1;i++){
        for(j=0;j<m1;j++){
            scanf("%d",&arr1[i][j]);
        }
    }
    printf("enter the values in array 2\n");
    for(i=0;i<n2;i++){
        for(j=0;j<m2;j++){
            scanf("%d",&arr2[i][j]);
        }
    }
    printf("addition is:\n");
    for(i=0;i<n2;i++){
        for(j=0;j<m2;j++){
            printf("%d",arr1[i][j]+arr2[i][j]);
        }
        printf("\n");
    }}
}

