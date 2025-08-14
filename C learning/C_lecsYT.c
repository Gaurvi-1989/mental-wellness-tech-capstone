#include<stdio.h>
// int main(){

//     return 0;
// }

// int main(){
//     char line[15]="united kingdom";
//     printf("%15.6s\n",line); //space before 
//     puts(line); //adds by default \n
//     printf("%-15.6s...\n",line); //space after united
//     printf("%s",&line[2]); //starts printing from line[2]
//     return 0;
// }


//  int main(){
// // code to get input of whole line
//     char line[60],charac;
//     int c=0;
//     do{
//         charac=getchar();
//         line[c]=charac;
//         c++;
//     } while (charac!='\n');
//     c=c-1;
//     line[c]='\0';
//     printf("\n %s",line);
//   // method 2
/*      char line[60];
        gets(line);
        printf("%s",line);
*/
//     return 0;
// }


// int main(){
//     int a[3][3]={6,2,5,7,3,4,9,0,1};
//     int *p;
//     p=a[0];
//     printf("%p   %p   %p  %p   %p",a,p,*a,a[0],&a);
//     printf("\n%d",**a);[]
//     return 0;
// }   

// // Function to check if number is palindrome
// int isPalindrome(int num) {
//     return num == reverseNumber(num, 0);
// }

// // Recursive function to reverse a number
// int reverseNumber(int num, int rev) {
//     if (num == 0)
//         return rev;
//     return reverseNumber(num / 10, rev * 10 + num % 10);
// }