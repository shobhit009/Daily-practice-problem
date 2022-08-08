import heapq

def sortk(arr,n,k):

    heap =  arr[:k+1]
    heapq.heapify(heap)

    index = 0
    for i in range(k+1,n):
        arr[index] = heapq.heappop(heap)
        index += 1
        heapq.heappush(heap,arr[i])

    while heap:
        arr[index] = heapq.heappop(heap)
        index += 1
    
    return arr

print (sortk([9,8,7,19,18],5,2))