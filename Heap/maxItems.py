


    
        
def heapify(arr,i,n):
    L = 2*i +1
    R = 2*i +2
    smallest = i
    if (L< n and arr[L]<arr[smallest] ):
        smallest = L
    if (R<n and arr[R]<arr[smallest]):
        smallest = R
    
    if (smallest != i):
        arr[smallest],arr[i] = arr[i],arr[smallest]
        heapify(arr,smallest,n)

def maxItems(arr,sum):
    if (len(arr) is None):
        return
    if (sum<=0):
        return
    n = len(arr)
    for i in range(n-2//2,-1,-1):
        heapify(arr,i,n)

    print(arr)    
    diff = sum
    count = 0
    while(diff>=arr[0] and n):
        count += 1        
        diff -= arr[0]
        print (diff)
        arr[0],arr[n-1] = arr[n-1],arr[0]
        n -= 1
        heapify(arr,0,n)
    print(arr)
    return count

res = maxItems([1,12,5,111,200],12)
print (res)
