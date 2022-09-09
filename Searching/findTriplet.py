def find_triplet(arr,n,x):
    h = n-1
    for i in range(n-2):
        l = i + 1
        curr_sum = x - arr[i]
        while (l < h):
            if arr[l] + arr[h] == curr_sum:
                print (arr[i], arr[l], arr[h])
                return True
            elif arr[l] + arr[h] > curr_sum:
                h -= 1

            else:
                l += 1

    return False

print (find_triplet([2,5,10,15,18],5,43))