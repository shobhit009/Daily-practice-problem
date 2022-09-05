# Idea : if binary array is given (array of 0 and 1) then two possibilities can happen 
# difference between group of 1's and 0's can be 1 or 0

# we always flip the second group element to achieve the minimum number of flips

def find_min_flip_group(arr,n):
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print ("From {} to".format(i),end = " ")
            else:
                print (i-1)

    if arr[n-1] != arr[0]:
        print (n-1)

find_min_flip_group([0,0,1,1,0,0,1,1,0,1],10)
