# print n to 1 using recursion -https://www.youtube.com/watch?v=qDJJBZAIXIw&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=4

def printnum(n):     # hypothesis: printing n to 1

    if n==0:         # base condition, smallest valid i/p 1
        return 

    print(n)          # induction step, it gives desired o/p for recusrion call on smaller i/p  .will print n before n-1, n-2...
    printnum(n-1)     # will print n-1, n-2, n-3..1

n=5

printnum(n)
    