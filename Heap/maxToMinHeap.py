# Given array representation of max Heap, convert it to min Heap in O(n) time. 
# Example : 
 
# Input: arr[] = [20 18 10 12 9 9 3 5 6 8] OR 
#        
#          20
#        /    \
#      18      10
#    /    \    /  \
#   12     9  9    3
#  /  \   /
# 5    6 8 
# Output: arr[] = [3 5 9 6 8 20 10 12 18 9]
#          3
#       /     \
#      5       9
#    /   \    /  \
#   6     8  20   10
#  /  \   /
# 12   18 9 





def min_heapify(arr,i,n):
    L = 2 * i + 1
    R = 2 * i + 2
    smallest = i

    if (L<n and arr[L]<arr[smallest]):
        smallest = L
    if (R<n and arr[R]<arr[smallest]):
        smallest = R
    if(smallest != i):
        arr[i],arr[smallest] = arr[smallest],arr[i]
        min_heapify(arr,smallest,n)    


def convert_to_min_heap(arr,n):
    for i in range(int((n-2)/2),-1,-1):
        min_heapify(arr,i,n)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [20, 18, 10, 12, 9, 9, 3, 5, 6, 8,12,13,45,6,6,16,7,9000.50000,46767,98890,9090]
    n = len(arr)
 
    print("Max Heap array : ")
    printArray(arr, n)
 
    convert_to_min_heap(arr, n)
 
    print("Min Heap array : ")
    printArray(arr, n)