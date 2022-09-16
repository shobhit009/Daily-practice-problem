# An inversion is a pair where in greater element occurs before the smaller element



def CountAndMerge(arr,l,m,r):
    # print (m)
    n1 = m-l+1
    n2 = r-m
    # 
    # print(n1)
    left =[None] * n1
    right = [None] * n2

    for i in range (n1):
        left[i] = arr[l + i]
    for j in range(n2):
        right[j] = arr[m+i+1]

    i = 0
    j = 0
    k = l
    res = 0

    while (i <n1 and j<n2):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res = res + (n1-i)

        k += 1
    while (i < n1):
        arr[k] = left[i]
        i += 1
        k += 1
    while (j < n2):
        arr[k] = right[j]
        j += 1
        k += 1
    return res

    
def MergeSort(arr,l,r):
    res = 0
    if l<r:
        mid = (l + r)//2
        # print (mid)
        res += MergeSort(arr,l,mid)
        res += MergeSort(arr,mid+1,r)
        res += CountAndMerge(arr,l,mid,r)
    return res

print (MergeSort([40,30,20,10],0,3))
    