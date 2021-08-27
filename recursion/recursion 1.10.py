# tower of hanoi- recusive way - https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11

# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
# 1) Only one disk can be moved at a time. 
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
# 3) No disk may be placed on top of a smaller disk.

#https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/

def TowerOfHanoi(n , source, destination, helper):

    if n==1:                                                                            # base condition, if only 1 disk, then transfer directly to dest
        print ("Move disk 1 from source",source,"to destination",destination)
        return

    TowerOfHanoi(n-1, source, helper, destination)                                       # call recursion on smaller i/p, n-1 disk, tranfer it from source to helper disk, here helper actas as destination 
    print ("Move disk",n,"from source",source,"to destination",destination)              # prints the moves from tranfering the disks. moving the last and lrgest disk from source to dest
    TowerOfHanoi(n-1, helper, destination, source)                                       # recursion call on n-1 disks placed in helper disk, here helper acts as source, and source acts as helper

n = 3
TowerOfHanoi(n,'A','B','C') 