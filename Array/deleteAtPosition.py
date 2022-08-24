def delete_at_position(arr,x,size,capacity):
    if size == 0:
        return 
    
    for i in range(size):
        if arr[i] == x:
            break
    # print (i)   
    if i == size-1:
        return "Element Not Found"
    
    for j in range (i,size-1):
        arr[j] = arr[j+1]

    arr[size-1] = None
    size -= 1

    return arr

print (delete_at_position([3,8,12,5,6],14,5,5))