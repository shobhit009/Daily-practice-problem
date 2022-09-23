def match_distinct_pattern(text,pat):
    n = len(text)
    m = len(pat)
    i = 0
    while(i < n-m+1):
        
        for j in range(m):
            if text[i+j] != pat[j]:
                break
            j += 1    
        if j==m:
            print (i)
            
        if j == 0:
            i += 1
        else:
            i += j

match_distinct_pattern("ABCABCD","ABCD")



