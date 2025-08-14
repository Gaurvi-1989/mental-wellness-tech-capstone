#include<stdio.h>
int main(){
    //multiplication
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
    int r2,c2;
    printf("enter rows and columns for 2nd matrix");
    scanf("%d %d",&r2,&c2);
    int arr2[r2][c2];
    for(int k=0;k<r2;k++){
        for(int l=0;l<c2;l++){
            printf("enter %d element in %d row ",l+1,k+1);
            scanf("%d",&arr2[k][l]);
        }
    }
    if (c!=r2)
        printf("multiplication is invalid");
    else {
        int mrr[r][c2];
        printf("multiplication matrix is: \n");
        for(int a=0;a<r;a++){
            for( int b=0;b<c2;b++){
                for(int x=0;x<c;x++){
                    mrr[a][b]+=arr[a][x]*arr2[x][b];
                }
                printf("%d ",mrr[a][b]);
            }
            printf("\n");
        }
    }
    return 0;
}