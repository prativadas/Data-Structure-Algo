#Print N-bit binary numbers having more 1’s than 0’s for any prefix- https://www.youtube.com/watch?v=U81n0UYtk98&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18
# Input:  N = 2
# Output: 11 10
# Explanation: 11 and 10 have more than or equal 1's than 0's(1's>=0's)

# we start with 1 always as if we start with 0, the even if we add any number of 1's, when we come to only {0}, the no. of 1's < no. of 0'

def solve(ones, zeros, n,output) :

    if n==0: 
        print(output)
        return

    output1 = output + '1'                              # choice for 1, from RT, we observe we always have the option to push 1's 
    solve(ones+1, zeros, n-1,output1)                   # when we choose 1, the count of 1 increases, no 0 used so no change, n always decreases                                         
    
    if (ones>zeros):                                     # choice for 0, when 1's > 0's then only we can add another 0
        output2 = output
        output2 = output + '0'
        solve(ones, zeros+1, n-1,output2)   
        return
    

if __name__ == '__main__':
                                        
    n = 3                               # number of bits 0/1          
    output = ''
    ones = 0                            # initialize 2 var for keeping count of 0's and 1's
    zeros = 0                     
    solve( ones, zeros,n,output)  

