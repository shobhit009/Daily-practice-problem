def maxPieces(n,a,b,c):
    if n == 0:
        return 0
    if n <a and n<b and n<c :
        return -1

    res = max(maxPieces(n-a,a,b,c),maxPieces(n-b,a,b,c),maxPieces(n-c,a,b,c))

    if res == -1:
        return -1
    else:
        return res + 1

    
print(maxPieces(9,2,2,2))