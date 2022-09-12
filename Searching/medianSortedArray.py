def find_median(arr1,arr2,m,n):
    i = 0
    j = 0
    arr = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    # print (i,j)
    while (i<m):
        arr.append(arr1[i])
        i += 1
    while (j<n):
        arr.append(arr2[j])
        j += 1

    x = m+n-1
    if x %2 == 0:
        res = arr[x//2]
    else:
        res = (arr[x//2] + arr[x//2+1])/2
    
    return res

if __name__ == "__main__":
    arr1 = [5,15,25,35,45]
    arr2 = [10,20,30,40,50]
    print (find_median(arr1,arr2,5,5))