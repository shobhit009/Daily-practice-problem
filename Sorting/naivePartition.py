def partition(arr,l,h,pivot):
    temp =[None]*(h-l)
    index = 0
   
    for i in range(l,h):
        if arr[i] <= arr[pivot]:
            temp[index] = arr[i]
            index += 1
    
    for i in range(l,h):
        if arr[i] > arr[pivot]:
            temp[index] = arr[i]
            index += 1

    for i in range(l,h):
        
        arr[i] = temp[i-l]

    return arr

print(partition([5,13,6,9,12,11,8],0,7,3))



    