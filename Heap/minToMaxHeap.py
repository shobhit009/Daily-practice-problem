# Given array representation of min Heap, convert it to max Heap in O(n) time. 
# Example : 
 

# Input: arr[] = [3 5 9 6 8 20 10 12 18 9]
#          3
#       /     \
#      5       9
#    /   \    /  \
#   6     8  20   10
#  /  \   /
# 12   18 9 


# Output: arr[] = [20 18 10 12 9 9 3 5 6 8] OR 
#        [any Max Heap formed from input elements]

#          20
#        /    \
#      18      10
#    /    \    /  \
#   12     9  9    3
#  /  \   /
# 5    6 8 


def max_heapify(arr,i,n):
    L = 2 * i + 1
    R = 2 * i + 2
    largest = i

    if (L<n and arr[L]>arr[largest]):
        largest = L
    if (R<n and arr[R]>arr[largest]):
        largest = R
    if(largest != i):
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,n)    


def convert_to_max_heap(arr,n):
    for i in range(int((n-2)/2),-1,-1):
        max_heapify(arr,i,n)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    n = len(arr)
 
    print("Min Heap array : ")
    printArray(arr, n)
 
    convert_to_max_heap(arr, n)
 
    print("Max Heap array : ")
    printArray(arr, n)