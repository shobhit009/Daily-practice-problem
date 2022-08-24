# def find_second_largest(arr,n):
#     largest = -float('inf')
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#             largest_index = i

#     second_largest = float('inf')
#     second_largest_index = -1
#     for i in range(n):
#         if arr[i]!=largest:
#             diff = largest-arr[i]
#             if diff < second_largest:
#                 second_largest = diff
#                 second_largest_index = i
#     return second_largest_index


def find_second_largest(arr,n):
    first_largest = 0
    second_largest = -1
   
    for i in range(n):
        if arr[i]>arr[first_largest]:
            second_largest = first_largest
            first_largest = i
        elif arr[i]<arr[first_largest]:
            if (second_largest ==-1 or arr[i] >arr[second_largest]):
                second_largest = i
    return second_largest

print (find_second_largest([20,20,10,20,20],5))