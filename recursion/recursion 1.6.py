# mid element deletion from stack using recursion- https://www.youtube.com/watch?v=oCcUNRMl7dA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=8

stack = []

stack.append(3)
stack.append(-6)
stack.append(21)
stack.append(5)
stack.append(0)
stack.append(5)
stack.append(1)

# print(stack)

# print(len(stack)-1)         # top elemnet

k = len(stack)//2 + 1          # when len(stack)= even, take floor value, // divides the odd numbers in python and takes int value 

class Del:

    def solve(self, stack, k):                      # hypothesis, k points to the middle element of stack

        if k == 1:                                  # base condition for solve(), we bring the mid element to top of stack to delete, k points to the mid element of stack

            stack.pop()
            return 

        temp = stack[len(stack)-1]             # we store top elemnt of stack in temp var, then pop it 
        stack.pop()
        self.solve(stack, k-1)                 # recursion call, here k is smaller i/p, when top elemnts are popped, k value decreases then finally k==1
        stack.append(temp)                     #append popped element to stack after deletio of mid element. #induction step, it gives desired o/p for recusrion call on smaller i/p 
        return

    def delMid(self, stack):

        if len(stack) == 0:                        # base condition for delMind(), when stack is empty

            return stack

        self.solve(stack, k)                      
        return stack

obj = Del()
print(obj.delMid(stack))