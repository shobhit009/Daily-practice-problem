def frequency(arr,n):
    count = 1
    for i in range(n-1):
        
        if (arr[i] == arr[i+1]):
            count += 1
        else:
            print (arr[i],count)
            count = 1
    print(arr[i+1],count)

frequency([10,10,10,10],4)