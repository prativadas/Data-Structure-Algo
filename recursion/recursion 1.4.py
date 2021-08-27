# sort array using recursion

# arr = [2, 3, 5, 4, 10, 3, 4, 5, 2, 1, -10, 0]

arr = [4,9,8,9, 2,2, 4, 3]

# print(type(arr))

# print(len(arr))

# print(type(len(arr)))

# print(arr[len(arr) - 1])

# print(type(arr[len(arr) - 1]))


# online code - https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6 - works as insertion sort

#You can't explicitly pass a variable by reference in Python, but you can update properties on existing objects.    

class Sorting:
 
    def insert(self, arr, temp):                                 # could have solved with loop but will go for recursion
        if len(arr) == 0 or arr[len(arr) - 1] <= temp:           # base condition, dont have to sort when arr is empty, or when last elemnt of array (largest value-when smaller i/p is sorted) <=  temp, the just append temp to arr,it will be sorted     
            arr.append(temp)                                      # temp value appended as it is to arr
            return
        
        val = arr[len(arr) - 1]               # when last element doesnt meet base condition, then stored in a temporary variable 'var', so next step, we pop last element      
        # print(val)
        arr.pop()                            # for applying recursion on smaller i/p,  last elememt of arr is popped, so and temp value can be inserted at right place of arr, then val is appended
        self.insert(arr, temp)
        arr.append(val)                     # induction step, it gives desired o/p for recusrion call on smaller i/p 
        

    def sort(self, arr):
        if len(arr) == 1:                       # when size of arr is 1 means it is already sorted, so return nothing
            return
        temp = arr[len(arr) - 1]                # last element of arr is stored in temp variable 

        # print(temp)
        arr.pop()                                # reducing array size/length in reverse for having smaller i/p for recursion, smallest valid i/p is 0
        self.sort(arr)                          # call sort() on arr of smaller i/p, when last element or arr is popped
        self.insert(arr, temp)                  # call insert(), to insert the temp at right place in arr 
        return arr
    

obj = Sorting()
print(obj.sort(arr))