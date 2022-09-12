def selection_sort(arr,n):
    for i in range(n-1):
        smallest = i
        swapped = False
        for j in range(i+1,n):
            if arr[j] < arr[smallest]:
                smallest = j
                swapped = True
        if (swapped):
            arr[i],arr[smallest] = arr[smallest],arr[i]
    return arr

print (selection_sort([10,5,8,20,2,18],6))

