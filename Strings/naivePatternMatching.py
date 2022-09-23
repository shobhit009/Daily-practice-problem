def match_pattern(txt,pat):
    n = len(txt)
    m = len(pat)

    # No. of iterations
    for i in range(n-m+1):
        # k is used to iterate pattern string
        k = 0
        # j will iterate txt in window length of pat string
        for j in range(i,i+m):
            if k == m-1 and pat[k] == txt[j]:
                print (i)
            # print ("j->",j)
            if txt[j] != pat[k]:
                break
            else:
                
                k += 1
                # print ("k->",k)

           

match_pattern("ABCABCD","AB")