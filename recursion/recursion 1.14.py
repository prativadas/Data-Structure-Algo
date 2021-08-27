# Permutation with spaces - https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14
#Input:
# S = "ABC"
# Output: (A B C)(A BC)(AB C)(ABC)

def solve(input, output):

    if len(input)==0:                  # base condition, when i/p string is empty, at leaf node of tree, all o/p are printed when i/p is empty
        print(output)
        return                         # at leaf node, if you call recursion after this then segmentation fault occur

    output1 = output                   # each i/p symbol we have 2 choice, so save it in 2 o/p, whether to include symbol with space or without space
    output2 = output

    output1 = output + '_'+ (input[0])     # choose symbol with space before
    output2 = output + input[0]            # choose symbol without space
    input = input[1:]                      # now make the i/p smaller by removing the symbol on which decision have been made.

    solve(input, output1)                  # then we call recursion on smaller o/ps
    solve(input, output2)

if __name__ == '__main__':
    input = 'ABC'                           # initialize i/p string
    output = ''                            # initialize o/p string to empty
    output += input[0]                     # as 1st element can be added as it is, with no space before(_A not allowed), so we divide o/p string and store 0th elemnt of i/p to o/p
    input = input[1:]                      #then new i/p will be BC, we delete the 0th element from i/p 
    solve(input, output)                   # call recursion now on new i/p