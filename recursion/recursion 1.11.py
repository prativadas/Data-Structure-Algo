#Print Subsets | Print PowerSets | Print all Subsequences - https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=13

def solve(input, output):

    if len(input)==0:                         # base condition, when i/p string is empty, at leaf node of tree
       print(output)
       return 

    output1 = output                        # see IP-OP tree for better understanding 2 o/p choices for each symbol whether to include it or not in o/p. from choice diagram output will produce 2 more o/p having output a common element in them
    output2 = output
                                             # o/p1 will be same as o/p, we choose not to include 0th index
    output2 += input[0]                       #o/p2 will have 0th index of i/p, as we are choosing to keep 0th index. use this line when i/p is str
    # output2 += str(input[0])                # when i/p str is int, use this line to convert i/p to str to concatenate with o/p2 str
    # output2.append(input[0])                # gives error as strings are not mutable

    input = input[1:]                         #strings are immutable, so you can't remove something from an existing string, just construct a new one.

                                              # now make the i/p smaller and call recursion on them

    solve(input, output1)
    solve(input, output2)

# Generates power set in lexicographic order
# def powerSet(input):
#     input = ''.join(sorted(input))
#     solve(input, len(input))

if __name__ == '__main__':
    input = 'abc'                    # initialize i/p string
    # input = [1, 2, 3]              # how to make this code work for intergers
    output = ''                      # initialize o/p string to empty, empty string is there but not showing separating in ''
    solve(input, output)