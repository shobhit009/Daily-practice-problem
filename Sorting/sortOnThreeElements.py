def sort (arr,n):
    lo = 0
    mid = 0
    hi = n-1

    while (mid<=hi):
        if arr[mid] == 0:
            arr[lo],arr[mid] = arr[mid],arr[lo]
            lo += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        else:
            arr[hi],arr[mid] = arr[mid],arr[hi]
            hi -= 1

    return arr
print (sort([0,2,1,0,1,2],6))