def maxGuest(arr,dep,n):
    arr.sort()
    dep.sort()

    i,j = 1,0
    res,curr = 1,1

   
    while (i<n and j<n):
         # if arrival time of next person is less than  departure time of previous person
        if arr[i] <= dep[j]:
            # increase current person count by 1 and check arrival of next person
            curr += 1
            i += 1
        else:
            # otherwise person has departed and decrease the person count by 1
            curr -= 1
            j += 1
        # res stores the max count of person seen till now
        res = max(res,curr)

    return res

print (maxGuest([800,700,600,500],[840,820,830,530],4))