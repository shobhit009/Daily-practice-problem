# iterative
def reverse_array(arr,n):
    i = 0
    j = n-1

    while (j>=i):
        arr[i],arr[j] = arr[j],arr[i]
        i +=1
        j -=1

    return arr

#recursive

def reverse_array_rec(arr,i,j):
    if (i >= j):
        return arr

    arr[i],arr[j] = arr[j],arr[i]    

    return reverse_array_rec(arr,i+1,j-1)


# print (reverse_array([1,2,3,4,5,6],6))

print (reverse_array_rec([1,2,3,4,5],0,4))