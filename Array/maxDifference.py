# def max_difference(arr,n):
#     max_diff = -float('inf')
#     for i in range (n-1):
#         for j in range(i+1,n):
#             if arr[j]-arr[i] > max_diff:
#                 max_diff = arr[j]-arr[i]

    # return max_diff

# Efficient
def max_difference(arr,n):
    res = arr[1]-arr[0]
    minVal = arr[0]

    for j in range(1,n):
        res = max(res,arr[j]-minVal)
        minVal = min(minVal,arr[j])

    return res

print(max_difference([30,10,8,2],4))