# k-th symbol grammar - https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10

# 0/p will either be 0/1, as Grammar generates strings of 0 and 1

# start with 0 , when 0 - replace with 0 1 in next row, when 1 - replace with 1 0 in next row

# #Row 1: 0
# Row 2: 01
# Row 3: 0110
# Row 4: 01101001                # 2nd half is the complement of 3rd row

class Findelement:

    def solve(self, N, k):                         # consider N = rows and k = cols

        if (N==1 and k ==1):                       # base condition
            return 0

        # mid = pow(2, N-1)               length of grammar

        mid = pow(2, N-1)//2

        if k <= mid:
            return self.solve(N-1, k)
        else:
            if(self.solve(N-1,k-mid)==0):                     # this way we can complement
                 return 1
            else:
                 return 0
            
            #  return self.solve(N-1, k-mid)                     #Induction, but we have to find the complement
        #    return ~self.solve(N-1, k-mid)                      # use complement of solve(N-1, k-mid), as we observe the pattern
 
                                                              #~ is a bitwise inversion operator, so instead of giving 1 it gives -1
obj = Findelement()
print(obj.solve(4, 8))