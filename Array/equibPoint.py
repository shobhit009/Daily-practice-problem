def compute_left_prefix(arr,n):
    prefix_sum_array=[None]*n
    sum = 0
    for i in range(n):
        sum += arr[i]
        prefix_sum_array[i] = sum

    return prefix_sum_array

def is_equib_point(arr,n):
    prefix_l_sum = compute_left_prefix(arr,n)
    prefix_r_sum = [None]*n
    sum = prefix_l_sum[n-1]
    for i in range(n):
        prefix_r_sum[i] = sum - arr[i]
        sum = sum - arr[i]

    for i in range(n):
        if i-1 < 0 and 0 == prefix_r_sum[i]:
            return True
        if prefix_l_sum[i-1] == prefix_r_sum[i]:
            return True
    return False

print (is_equib_point([5,6,20,-9],4))
        
