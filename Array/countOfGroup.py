
def count_of_group(arr,n):
    res = {0:0,1:0}
    prev_ele = 0

    i = 1
    while i < n:
        if arr[i] != prev_ele:
            res[prev_ele] += 1
            prev_ele = arr[i]
        
    
        i += 1
        if i == n-1:
            res[arr[n-1]] += 1
            
        
    return res

print (count_of_group([0,0,1,1,1,0,0,1,1,0,1,1,0],13))