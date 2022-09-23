def check_subsequence(string1,string2):
    i,j = 0,0
    while (i <len(string1) and j<len(string2)):
        if string1[i] == string2[j]:
            i += 1
            j += 1
        else:
            i += 1

    print (i,j)
    if j!= len(string2):
        return False
    else:
        return True
# subsequence doesn't necessarily mean that it should be contiguous

print (check_subsequence("ShobhitSharma","hohtrm"))
