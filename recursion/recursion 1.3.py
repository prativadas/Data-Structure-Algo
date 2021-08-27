# factorial using recursion, n! = n*n-1*n-2..*2*1 or n* (n-1)!

def fact(n):             ## hypothesis: prints n*n-1*n-2..to 1

    if n==0 or n==1:             # base condition, smallest valid i/p 1
         return 1
    
    return n*fact(n-1)    # fact(n-1) prints n-1*n-2*...to 1   
   
n = 5
print(fact(n))