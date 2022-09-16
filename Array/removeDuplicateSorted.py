def remove_duplicate(arr,n):
    count = 1
    for i in range(1,n):
        if arr[count-1] != arr[i]:
            arr[count] = arr[i]
            count +=1
   

        
    print (count)

def size_after_duplicate_removal(arr,n):
    count = 1
    i = 0 
    j= 1
    while (i<n and j < n):
        if arr[i] != arr[j]:
            count += 1
            i = j
            j += 1
        else:
            j += 1
    return count


print (size_after_duplicate_removal([10,10,10],3))

    

