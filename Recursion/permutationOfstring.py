

def permutation(string,i):
    if i == (len(string)-1):
        print (string)
        return
    for j in range(i,len(string)):
        string[i],string[j] = string[j],string[i]
        permutation(string,i+1)
        string[i],string[j] = string[j],string[i]

permutation(list("ABC"),0)