def count_counsecutive_ones(arr,n):
    count = 0
    curr_count = 0
    for i in range(n):
        if arr[i] == 1:
            curr_count += 1
            count = max(count,curr_count)
        else:
            
            curr_count = 0

        # count = max(count,curr_count)
    return count

print (count_counsecutive_ones([0,1,1,0,1,0],6))
