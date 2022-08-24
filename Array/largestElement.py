def find_largest(arr,n):
    largest = -float('inf')
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return index

print (find_largest([40,8,50,999],4))