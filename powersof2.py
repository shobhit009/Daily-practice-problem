
def powersof2(n):
    if n <1:
        return 0
    elif n == 1:
        # print (1)
        return 1
    else:
        prev = powersof2(n//2)
        # print (prev)
        curr = prev * 2
        print(curr)
        return curr

powersof2(8)