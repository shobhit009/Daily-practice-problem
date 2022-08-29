def left_rotate_by_d(arr,n,d):
    if d == 0:
        return arr
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = temp
    return left_rotate_by_d(arr,n,d-1)
    
# Efficient approach

def left_rotate(arr,n,d):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return  arr


def reverse(arr,low,high):
    while(low<high):
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1
print(left_rotate([1,2,3,4,5],5,3))