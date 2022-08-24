# def isSorted(arr,n):
#     if n == 1:
#         return True
#     for i in range(1,n+1):
#         if arr[i] < arr[i-1]:
#             return False
    
#     return True

def isSorted(arr,n):
    if n == 1:
        return True

    for i in range(n-1):
        if arr[i+1] < arr[i]:
            return False
    return True

print (isSorted([12,12,12,12,12,6],6))