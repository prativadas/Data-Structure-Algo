# sort a stack using recursuion - similar to array sort problem

# stack is a LIFO DS

stack = []

stack.append(3)
stack.append(-6)
stack.append(21)
stack.append(5)
stack.append(0)
stack.append(5)

# print(len(stack)-1)         # top elemnet

# print(stack)

# print(type(stack))

class Sorting:

    def insert(self, stack, var):                           

        if len(stack) == 0 or stack[len(stack)-1] <= var:                      
            stack.append(var)
            return

        var1 = stack[len(stack)-1]
        # print(var1)   
        stack.pop()
        self.insert(stack, var)        
        stack.append(var1)                 #induction step, it gives desired o/p for recusrion call on smaller i/p 

    def sortStack(self, stack):
        if len(stack) == 1:                                            
            return
        var = stack[len(stack)-1]     
        # print(var)          
        stack.pop()
        self.sortStack(stack)
        self.insert(stack,var)
        return stack

obj = Sorting()
print(obj.sortStack(stack))