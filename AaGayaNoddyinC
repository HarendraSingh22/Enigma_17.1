#include <cmath>
#include <bits/stdc++.h>
#include <cstdio>
#include <iostream>
#include <bitset> 
#include <vector>
#include <bitset>
#include <string>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#define INT_BITS 32
using namespace std;
int rightShift(int n,int l)//finally after wasting more than 1.5 hrs to search , coding by self
{
    int ld=n%10;
    n=n/10;
    n=(ld*pow(10,l-1))+n;
    return n;
}
int binaryToDecimal(int n)//http://www.geeksforgeeks.org/program-binary-decimal-conversion/
{
    int num = n;
    int dec_value = 0;
     
    // Initializing base value to 1, i.e 2^0
    int base = 1;
     
    int temp = num;
    while(temp)
    {
        int last_digit = temp % 10;
        temp = temp/10;
         
        dec_value += last_digit*base;
         
        base = base*2;
    }
     
    return dec_value;
}

int main() 
{
    int T,c,l;
    int binarynum;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        binarynum=0;
        scanf("%i",&binarynum);
        c=0;
        l=(to_string(binarynum)).length();
        
       
     
        for(int j=0;j<l;j++)
        {
            
            int number=binaryToDecimal(binarynum);
            
            if(number%2==0)
               c++;
            binarynum=rightShift(binarynum,l);
        }
       printf("%d",c);
        
        
      
        
        
    }
    
    
    return 0;
}



//*Help Doc* By {HS}
// printf("\nRight Rotation of %d by %d is ", n, d);
// printf("%d", rightRotate(n, d));

