# Python code for Josephus Problem
def solve(k, i, A):
    if len(A) == 1:
        print(A)
        return A[0]
    idx = (i + k - 1) % len(A)
    A.pop(idx)
    return solve(k, idx, A)

n = 40
k = 7
i = 0
A = [i+1 for i in range(n)]                     # A is a list consisting people from 1 to n
# print(type(A))
# print(A)
    
output = solve(k, i, A)
print(output)