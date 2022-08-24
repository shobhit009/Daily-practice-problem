def insert_at_position(arr,x,pos,size,capacity):
    if size == capacity:
        return False


    for i in range(size-1,pos-2,-1):
        print (i)
        arr[i+1] = arr[i]

    arr[pos-1] = x
    size += 1

    return arr

print (insert_at_position([5,7,10,20,None],3,2,4,5))