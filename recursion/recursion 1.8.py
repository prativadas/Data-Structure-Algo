# Reverse a Stack using Recursion - without using extra space menas extra stack - https://www.youtube.com/watch?v=8YXQ68oHjAs&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=9

stack = []

stack.append(3)
stack.append(-6)
stack.append(21)
stack.append(5)
stack.append(0)
stack.append(5)
stack.append(1)

# print(len(stack)-1)         # top elemnet

class Reverse:

   def insert(self, stack, var):

       if len(stack) == 0:                        # base condition when stack is empty, var value appended as it is to stack
          stack.append(var)                       # push var as it is on top of stack, var is a variable defined in reverse(), that stores the top of stack

          return

       temp = stack[len(stack)-1]                # when if condition is false: again top of stack(not the one stored in var) stored in temp before popping it
       stack.pop()

       self.insert(stack, var)                   # recursion applied on smaller i/p of stack
       stack.append(temp)                        # append popped element as it is when all elements are reversed

       return

   def reverse(self, stack):

       if len(stack) == 1:                      #  # when size of stack is 1 means nothing to do
           return 

       var = stack[len(stack)-1]               #last element of arr is stored in var variable and pop it from stack
       stack.pop()

       self.reverse(stack)                     # recursion call on smller i/p of stack with reverse()
       self.insert(stack,var)                  # induction step using another recursion: insert(), to insert the var at right place in stack    
       return stack

obj = Reverse()
print('original stack', stack)
print('reversed stack', obj.reverse(stack))
    
