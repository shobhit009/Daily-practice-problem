# Moore's Voting algorithm

def find_majority(arr,n):
    res = 0 
    count = 1
    for i in range(1,n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1

        if (count == 0):
            res = i 
            count = 1
    
    count = 0
    for i in range(n):
        if arr[res] == arr[i]:
            count += 1
      
    if count <= n/2:
            res= -1

    return res

print(find_majority([6,8,7,6,6],5))