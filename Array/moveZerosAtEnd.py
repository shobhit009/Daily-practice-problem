def moveZero(arr,n):
    count = 0 # keep track of Non-zero elements
    
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count += 1

    return arr

print (moveZero([8,5,0,10,0,20],6))