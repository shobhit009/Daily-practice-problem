def insertion_sort(arr,n):
    for i in range(1,n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j],arr[i] = arr[i],arr[j]

    return arr

print (insertion_sort([10,5,8,20,2,18],6))

