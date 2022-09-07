def binarySearch(arr,l,h,key):
    mid = (l+h)//2
    # print (mid)
    if l> h:
        return -1
    
    if key > arr[mid]:
       return binarySearch(arr,mid+1,h,key)
    elif key < arr[mid]:
        return binarySearch(arr,l,mid-1,key)
    else: 
        if mid == h or arr[mid] != arr[mid+1]:
            return mid
        else:
            return binarySearch(arr,mid+1,h,key)
   
    
print (binarySearch([15,15,15],0,2,15))
