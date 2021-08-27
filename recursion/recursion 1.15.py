#Permutation with Case Change | Recursion - https://www.youtube.com/watch?v=J2Er5XceU_I&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15

# Input : ab
# Output : AB Ab ab aB

def solve(input, output):

    if len(input)==0:                  # base condition, when i/p string is empty, at leaf node of tree, all o/p are printed when i/p is empty
        print(output)
        return

    output1 = output                     # we have 2 choices for a i/p symbol, either take small case or captical case
    output2 = output

    output1 = output + input[0]            # when o/p was empty, we choose small case of 0th index and add it to o/p1   
    output2 = output + input[0].upper()    # we add upper case of 0th index to o/p2

    input = input[1:]                      # remove 0th index from i/p string as we have made decision for it, now call recursion for nrex symbol

    solve(input, output1)                  # then we call recursion on smaller o/ps
    solve(input, output2)


if __name__ == '__main__':
    input = 'ab'                           # initialize i/p string
    # input = 'aB'                         # will not work as we are assuming here we have i/p with all lower case
    output = ''                            # initialize o/p string to empty           
    solve(input, output)  