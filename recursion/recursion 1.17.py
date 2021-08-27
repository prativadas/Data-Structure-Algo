# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"] - https://leetcode.com/problems/letter-case-permutation/

# def solve(input, output, vector): - error coming find out why when you want to store o/p in a vector
def solve(input, output):

    if len(input)==0:
        print(output)
        return                              # in leetcode ,we are asked return vector of string but we print o/p here
        

    if input[0].isalpha():                     # check if i/p symbol is a aplhabet    

         output1 = output 
         output2 = output
         output1 = output + input[0].lower()
         output2 = output + input[0].upper() 

         input = input[1:]  
 
         solve(input, output1)                  # then we call recursion on smaller o/ps, 2 recursive calls when i/p symbol is alphabet
         solve(input, output2)
    else:                                        # if the i/p symbol is a digit
        output1 = output
        output1 = output + input[0]

        input = input[1:]                          # make the i/p string smaller

        solve(input, output1)                       # recursion call wwhen i.p symbol is digit

if __name__ == '__main__':
    input = 'a1B2'                           # initialize i/p string
    output = ''                            # initialize o/p string to empty           
    # vector =  ['']                       # How to initialize a vector??
    solve(input, output)  