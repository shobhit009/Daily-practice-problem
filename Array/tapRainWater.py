def tapWater(arr,n):
    lmax = [None]*n
    rmax = [None]*n
    lmax[0] = arr[0]
    res = 0

    for i in range(1,n):
        lmax[i] = max(arr[i],lmax[i-1])
    
    rmax[n-1] = arr[n-1] 
    for i in range(n-2,-1,-1):
        rmax[i] = max(arr[i],rmax[i+1])

    for i in range(1,n-1):
        res += min(lmax[i],rmax[i])-arr[i]

    return res

print (tapWater([3,0,1,2,5],5))