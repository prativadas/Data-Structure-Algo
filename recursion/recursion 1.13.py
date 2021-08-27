##Print Subsets | Print PowerSets | Print all Subsequences -  https://www.youtube.com/watch?v=mEBEw_xScsE

#https://stackoverflow.com/questions/19398993/typeerror-can-only-concatenate-list-not-str-to-list

def findPowerSet(S, i, curr):                       # S = string, i = current index, curr= current string/ subset

    if i == len(S):                                  # base condition, when index surpasses max index value means > len(s)
        print(curr)                                  # then print current subset as we hit the leaf of tree, then we return
        return
    findPowerSet(S, i+1, curr + [S[i]])            #recursion call on next index, we choose to add s[i] to curr  #error is you are adding string and list, you should use list or [] to make the string become list type. #use '[S[i]]' or list([S[i]]) instead of S[i]
    findPowerSet(S, i+1, curr)                     # we call this recursion when the 1st recursion call ran for complete len(s), here we dont add s[i] to curr string
    
# # Generates power set in lexicographic order
# def powerSet(S):
#     S = ''.join(sorted(S))
#     findPowerSet(S, len(S))

if __name__ == '__main__':
 
    # S = 'abc'

    S = [1, 2, 3]
 
    curr = []                         # initialize current string as empty and current index at 0
    findPowerSet(S, 0, curr)