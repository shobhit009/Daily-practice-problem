def min_difference(arr,n):
    res = float('Inf')
    arr = sorted(arr)
    for i in range(1,n):
        res = min(res,arr[i]-arr[i-1])
    
    return res

print (min_difference([1,8,12,5,18],5))