def union_of_array(arr1,arr2):
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0

    while (i < n and j < m):
        if i > 0 and (arr1[i] == arr1[i-1]):
            i += 1
            continue

        if j > 0 and (arr2[j] == arr2[j-1]):
            j += 1
            continue
            
        if arr1[i] < arr2[j] :
            print (arr1[i])
            i += 1

        elif arr1[i] == arr2[j]:
            print (arr1[i])
            i += 1
            j += 1

        else:
            print (arr2[j])
            j +=1 

    while (i<n):
        if arr1[i] != arr1[i-1]:
            print (arr1[i])
            i += 1
        else:
            i += 1
            continue


    while (j<m):
        if arr2[j] != arr2[j-1]:
            print (arr2[j])
            j += 1
        else:
            j += 1
            continue

union_of_array([3,5,8],[2,8,9,10,10,15])

