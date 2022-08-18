def heapify(arr,i,n):
    L = 2*i + 1
    R = 2*i + 2
    smallest = i

    if (L<n and arr[L] < arr[smallest]):
        smallest = L
    if (R < n and arr[R]<arr[smallest]):
        smallest = R
    
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,smallest,n)



def klargest(arr,k):
    n = len(arr)
    for i in range (k//2, -1,-1):
        heapify(arr,i,k)

    # print (arr)
    for i in range(k,n):
        if arr[i] > arr[0]:
            arr[0],arr[i] = arr[i],arr[0]
            # print("befoe heapify", arr)
            heapify(arr,0,k)
            # print (arr)
      
    

    return arr[:k]

if __name__ == "__main__":
    arr = [5,15,10,20,8]
    k = 3

    print(klargest(arr,k))





