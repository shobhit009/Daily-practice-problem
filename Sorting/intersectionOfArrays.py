def intersection_of_two_arrays(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    last_printed_element = float('inf')

    for i in range(n):
        if arr1[i] != last_printed_element and arr1[i] in arr2:
            print (arr1[i])
            last_printed_element = arr1[i]





def find_intersection(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    last_printed_element = float('inf')
    i = 0
    j = 0

    while (i < n and j<m):
        if arr1[i] < arr2[j]:
            i += 1
        elif (arr1[i] == arr2[j] and arr1[i] != last_printed_element):
            print (arr1[i])
            last_printed_element = arr1[i]
            i += 1
            j += 1
        else:
            j += 1


    

find_intersection([2,20,20,40,60],[10,20,20,20])