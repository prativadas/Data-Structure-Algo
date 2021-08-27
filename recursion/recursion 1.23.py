def solve (output,k, index, ans):
    if len(output)==1:                        
        ans = output[0]
        print(ans)
        return ans

    index = (index + k) % len(output)
    output.pop(index)                                   

    solve (output,k, index, ans) 

if __name__ == '__main__':
    
                                        
    input = 5                               
    k= 2                                    
    output = [i+1 for i in range(input)]
    index = 0                              
    ans = -1                               
    k= k-1                                   
                                
    solve(output,k, index, ans)