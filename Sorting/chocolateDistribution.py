# Distribute chocolates into m groups such that difference b/w max chocolate given and min chocolate given is minimum

def find_min_diff(arr,n,m):
    if m>n:
        return -1
    res = float('Inf')
    arr.sort()
    for i in range(n-m+1):
        res = min(res,arr[i+m-1]-arr[i])

    return res

print (find_min_diff([7,3,2,4,9,12,56],7,3))

