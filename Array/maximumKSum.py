def maximum_k_sum(arr,n,k):
    res = 0
    for i in range (n):
       curr_sum = 0
       for j in range (i,i+k):
           if i+k < n:
               curr_sum += arr[j]
               res = max(res,curr_sum)

    return res


def sum(arr,n,k):
    '''idea is to compute sum of first k elements , then  run a loop for k to n, k will be the 
        last element of current sliding window (window after first slide)
        add this element to the previous computed sum
        subtract the previuos index sum arr[i-k]
    '''
    res = 0 
    curr_sum = 0

    for i in range(k):
        curr_sum += arr[i]

    res = curr_sum
    print (res)
    for i in range (k,n):
        curr_sum = curr_sum + arr[i] - arr[i-k]
        res = max(res,curr_sum)

    return res
print(sum([1,8,30,-5,20,7],6,3))

