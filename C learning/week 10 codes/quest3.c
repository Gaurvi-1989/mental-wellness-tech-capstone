#include<stdio.h>
int main(){
    //input 2d array
    int r,c;
    printf("enter rows and columns");
    scanf("%d %d",&r,&c);
    int arr[r][c];
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            printf("enter %d element in %d row ",j+1,i+1);
            scanf("%d",&arr[i][j]);
        }
    }
    for(int k=0;k<r;k++){
        for(int l=0;l<c;l++){
            printf("%d ",arr[k][l]);
        }
        printf("\n");
    }
    return 0;
}