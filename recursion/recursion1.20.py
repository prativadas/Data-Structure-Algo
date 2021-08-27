#Josephus Problem | Game of Death in a circle | Execution in Circle - https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19

#https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle1840/1

# n people standing in a circle (numbered clockwise 1 to n) waiting to be executed. The counting begins at point 1. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom.
# Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle.
# without using cicular queue, here we use array and give logic to access index at starting from th end of array(edge conditions), (currentindex + k)% (current array size)
# we will solve this using IBH method, induction step not required as we dont want to use nodes thats already remvoved.
# when n=5, k=3, means we start counting from 0th index and delete the 2nd index(means 3rd element), we do k=k-1(3-1=2).
# so we first do k=k-1, then we remove the person at (currentindex + k), 

def solve (output,k, index, ans):
    if len(output)==1:                           # base condition
        ans = output[0]
        print(ans)
        return ans
    #we always kill (index + k)th person- here k is actually k-1 that we did in main()
                                          
    index = (index + k) % len(output)                  # if we use a array to represrent position of people instead of circle, the at some point, we get segmentation fault as the next index is not avilable we wan to kill in the array, so use module to get next index of kth element to be killed
    output.pop(index)                                   # pop those killed every time, making the list smaller. person who is killed is at (index+k)

    solve (output,k, index, ans)                       # call recursion on smaller i/p

if __name__ == '__main__':
    # safe person should be at position 3, for input=5, k=2, for input=40, k=7 , safe position is 24
                                        
    input = 5                               # total number of people        
    k= 2                                    # every 2nd person from curent index has be removed. 
    output = [i+1 for i in range(input)]
    index = 0                               # initialize with 0, and every (index + k)th person will be killed, here k is actually k-1
    ans = -1                                 # ans will return output[0], person alive at last
    k= k-1                                   # from 0th index, we count it as 1, so person to be removed is at kth position is actually at k-1 position 
                                       
    # i=0  
    # output = []                        - why this way of initializing output list is not working                    
    # for i in range(input):
    #     output = output + [i]
    #     # output.append(i)                    
    # print(output)
    # print(type(output))
                                
    solve(output,k, index, ans)
    
  