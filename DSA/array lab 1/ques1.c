#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int i,j;
    int arr[n][n];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("enter the values in array");
            scanf("%d",&arr[i][j]);
        }
    }
    printf("array is:\n");
    int sum=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ",arr[i][j]);
            sum+=arr[i][j];
        }
        printf("\n");
    }
    printf("sum of elements of 2D array is : %d",sum);
}