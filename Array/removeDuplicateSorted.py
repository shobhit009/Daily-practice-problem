def remove_duplicate(arr,n):
    count = 1
    for i in range(1,n):
        if arr[count-1] != arr[i]:
            arr[count] = arr[i]
            count +=1
   

        
    print (count)


print (remove_duplicate([10,10,20,20],4))

    

