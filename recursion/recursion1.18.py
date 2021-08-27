# Generate all Balanced Parentheses- https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()" - here we have choice for each bracket, either choose open or close, decision should be made in a way that o/p is balanced


def solve(open, close, output):                       # number of open (, and close )

   if open==0 and close==0:
        print(output)
       # vector = vector + output                       # how to push output to vector?
        return

   if (open!=0):                                         # from recursion tree, we notice, we push ( whenever its count is not 0, we always have the option to push (
        output1 = output
        output1 = output + '('
        solve(open-1,close, output1)                       # as we always start with (, so we reduce 1 from it. starting from ) will never be balanced

   if (close > open):                                     # from recursion tree, we notice when ) > ( - then only we push )
       output2 = output
       output2 = output + ')'
       solve(open,close-1, output2)
       return



      

# vector[string] fun(n)

if __name__ == '__main__':
                                        # initialize i/p string
    open = 3                           # initialize o/p string to empty           
    close = 3
    output = ''
    # vector =  []                       # How to initialize a vector??
    solve(open, close,output)  


