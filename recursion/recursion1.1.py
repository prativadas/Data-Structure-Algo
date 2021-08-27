# print 1 to n using recursion- https://www.youtube.com/watch?v=Xu5RqPdABRE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=3

# https://stackoverflow.com/questions/17127355/python-recursive-function-that-prints-from-0-to-n/49274410

def printnum(n):      # hypothesis: pinting 1 to n

    # if n==0:         # base condition, smallest valid i/p
    #     return 1      # return n also works
    
    
    if n==0:         # base condition, smallest valid i/p
        return 
    
    printnum(n-1)    # induction step fo printing 1 to n-1. induction step, it gives desired o/p for recusrion call on smaller i/p 

    print(n)          # printing n afte n-1, induction step

    # if n != 0:     or if n > 0:
    #     printnum(n-1) 
    #     print(n)  


n=10

printnum(n)
