def get_sum_precompute(arr,n):
    prefix_sum_array=[None]*n
    sum = 0
    for i in range(n):
        sum += arr[i]
        prefix_sum_array[i] = sum

    return prefix_sum_array

def get_sum(arr,n,l,r):
    precomputedSum = get_sum_precompute(arr,n)
    if l == 0:
        return precomputedSum[r]
    else:
        return precomputedSum[r]-precomputedSum[l-1]

print(get_sum([2,8,3,9,6,5,4],7,1,3))