def max_normal_sum(arr,n):
    max_sum = arr[0] 
    curr_sum = arr[0]
    for i in range (1,n):
        curr_sum += arr[i]

        if max_sum < curr_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum

def max_over_all(arr,n):
    max_normal = max_normal_sum(arr,n)
    if max_normal < 0:
        return max_normal

    arr_sum = 0
    for i in range(n):
        arr_sum += arr[i]
        arr[i] = -arr[i]

    max_circular = arr_sum + max_normal_sum(arr,n)

    return max(max_normal,max_circular)

print (max_over_all([8,-3,9,-5,12],5))
