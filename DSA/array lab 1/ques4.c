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
    if(m1!=n2){
        printf("cannot be multiplied because n1 and m2 are not same");
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
    printf("multiplication matrix is \n");
    for(i=0;i<n1;i++){
        for(j=0;j<m2;j++){
            int sum=0;
            for(int k=0;k<m1;k++){
            sum+=arr1[i][k]*arr2[k][j];
            }
            printf("%d  ",sum);
        }
        printf("\n");
    }
}
}