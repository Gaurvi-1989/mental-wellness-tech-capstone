#include<stdio.h>
int main(){
    int n;
    printf("enter number:");
    scanf("%d",&n);
    for(int i=2;i<=n;i++){
        int count=0;
        if (n%i==0){ 
            for(int k=1;k<=i;k++){
                if(i%k==0) count++;
            }
            if (count==2) {
                printf("\nprime factor is %d",i);
            }
        }
        else continue;
    }
    return 0;
}