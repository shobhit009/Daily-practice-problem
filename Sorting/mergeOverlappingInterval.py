def mergeInterval(arr,n):
    arr.sort(key=lambda x:x[0])
    index = 0

    for j in range(1,n):
        if arr[j][0] <= arr[index][1]:
            arr[index][0] = min(arr[index][0],arr[j][0])
            arr[index][1] = max(arr[index][1],arr[j][1])

        else:
            index += 1
            arr[index] = arr[j]

    for i in range(index+1):
        print (arr[i])


mergeInterval([[5,10],[3,15],[18,30],[2,7]],4)
