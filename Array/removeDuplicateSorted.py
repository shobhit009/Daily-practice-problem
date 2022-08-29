def remove_duplicate(arr,n):
    count = 1
    for i in range(1,n):
        if arr[count-1] != arr[i]:
            arr[count] = arr[i]
            count +=1
   

        
    print (count)
    return arr

print (remove_duplicate([10,20,20,20,30,30,30,30],7))

    

