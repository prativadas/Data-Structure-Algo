# from collections import deque
 
# Function to generate a power set of given set `S`- https://www.techiedelight.com/generate-power-set-given-set/

def findPowerSet(S, set, n):                        # S= i/p string, set= o/p subset, n= length
 
    # if we have considered all elements
    if n == 0:                               
        print(set)
        return
 
    # consider the n'th element
    set.append(S[n - 1])
    findPowerSet(S, set, n - 1)
 
    set.pop()                    # backtrack
 
    # or don't consider the n'th element
    findPowerSet(S, set, n - 1)
 
 
if __name__ == '__main__':
 
    S = [1, 2, 3]
 
    set = []
    findPowerSet(S, set, len(S))
 