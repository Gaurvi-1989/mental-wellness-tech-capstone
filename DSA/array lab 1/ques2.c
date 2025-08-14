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
    printf("transpose is:\n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ",arr[j][i]);
        }
        printf("\n");
    }
}