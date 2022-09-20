def checkPalindrom(string):
    i = 0
    j = len(string)-1

    while (i <=j):
        if (string[i] == string[j]):
            i += 1
            j -= 1
        else:
            return False
            
    return True

def check_palindrome_recurscive(string, i, j):
    if i==j:
        return True
    if string[i] != string[j]:
        return False
        
    return check_palindrome_recurscive(string, i+1, j-1)    

print (checkPalindrom("xBxzaxBx"))