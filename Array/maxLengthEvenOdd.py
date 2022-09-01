def max_length_even_odd_array(arr,n):
    max_length = 0
    curr_length = 0
    evenFlag = True
    oddFlag = True
    for i in range(n):
        if (evenFlag and arr[i] %2 == 0):
            curr_length += 1
            if max_length < curr_length:
                max_length = curr_length
                evenFlag = False
                oddFlag = True
        elif (oddFlag and arr[i] %2 != 0):
            curr_length += 1
            if max_length < curr_length:
                max_length = curr_length
                evenFlag = True
                oddFlag = False
        elif (oddFlag == False and arr[i]%2 != 0):
            curr_length = 0
            oddFlag = True
        elif (evenFlag == False and arr[i] %2 == 0):
            curr_length = 0
            evenFlag = True
    return max_length

def max_length(arr,n):
    max_length = 1
    curr_length = 1
    for i in range(1,n):
        if ((arr[i]%2 == 0 and arr[i-1]%2 != 0) or (arr[i]%2 != 0 and arr[i-1]%2 == 0)):
            curr_length +=1
            max_length = max(max_length,curr_length)
        else:
            curr_length = 1

    return max_length

print (max_length([10,12,14,7,8],5))