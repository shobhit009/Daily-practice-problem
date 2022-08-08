def generate_string_subsequence(s,curr,idx):
    if idx == len(s):
        print (curr)
        return
    
    generate_string_subsequence(s,curr,idx+1)
    generate_string_subsequence(s,curr+s[idx],idx+1)

generate_string_subsequence("ABC","",0)