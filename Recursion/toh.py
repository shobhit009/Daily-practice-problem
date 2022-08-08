def toh(n,a,b,c):
    if n==1:
        print ("Move Disc{} from {} to {}".format(n,a,c))
        return
    toh (n-1,a,c,b)
    print ("Move Disc{} from {} to {}".format(n,a,c))
    toh(n-1,b,a,c)

toh(4,"a","b","c")