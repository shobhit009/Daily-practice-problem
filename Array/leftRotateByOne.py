def left_rotate_by_one(arr,n):
    if n==1:
        return arr
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = temp

    return arr

print (left_rotate_by_one([1,2,3,4,5,6],6))