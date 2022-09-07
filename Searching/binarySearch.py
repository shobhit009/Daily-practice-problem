def binarySearch(arr,l,h,key):
    mid = (l+h)//2
    # print (mid)
    if l> h:
        return -1
    if arr[mid] == key:
        return mid
    if key > arr[mid]:
       return binarySearch(arr,mid+1,h,key)
    else :
        return binarySearch(arr,l,mid-1,key)
   
    

print(binarySearch([10,20,30,40,50,60],0,5,90))