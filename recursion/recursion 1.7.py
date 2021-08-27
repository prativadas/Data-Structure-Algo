# another way - found online - shorter code than what i wrote

data=[1,2,3,4,5]

def d(data,n,counter):

  if(len(data)):                   # base condition, if condition is false and exists when len(data) = 0, and returns nothing

    if(n==counter):                # assume n is mid element, if counter points to mid element then pop it from stack
      data.pop()                   # when above if condition is true, means we found mid element, pop it from stack
      return
      
    l=data.pop()                # if inner if loop is false, means we havent found mid element. so we pop top elemnts of stack and storing them in l
    d(data,n,counter+1)         # increase couter till we find mid elemnt
    data.append(l)              # finally append popped element at top of stack after del of mid element
  return data
  

print(d(data,len(data)//2,0))