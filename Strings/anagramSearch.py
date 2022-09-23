MAX = 256
def areSame(arr1,arr2):
    for i in range (MAX):
        if arr1[i] != arr2[i]:
            return False
    return True
    

def isPresent(text,pat):
    n = len(text)
    m = len(pat)

    dic_CT = [0] * MAX
    dic_CP = [0] * MAX

    for i in range(m):
        dic_CT[ord(text[i])] += 1
        dic_CP[ord(pat[i])] += 1

    for i in range (m,n):
        if areSame(dic_CT,dic_CP):
            return True
        dic_CT[ord(text[i])] += 1
        dic_CT[ord(text[i-m])] -= 1
            
    return False

print (isPresent("geeksforgeeks","frog"))

