def isSubArray(arr,n,sum):
    s = 0 
    curr = 0
    for i in range(n):
        curr += arr[i]
        while(curr>sum):
            curr -= arr[s]
            s += 1

        if curr == sum:
            return True
    return False

print (isSubArray([1,4,0,0,3,10,5],7,7))
