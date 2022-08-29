def print_leaders(arr,n):
    curr_leader = arr[n-1]
    print (curr_leader)
    for i in range(n-2,-1,-1):
        print (i,"->")
        if arr[i] > curr_leader:
            curr_leader = arr[i]
            print (curr_leader)

print (print_leaders([7,10,4,10,6,5,3,2],8))