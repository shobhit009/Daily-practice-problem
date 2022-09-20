def check_if_anagram(string1,string2):
    n1 = len(string1)
    n2  = len(string2)
    if n1 != n2:
        return False

    char_count = [0]*26

    for i in range(n1):
        char_count[ord(string1[i])-ord('a')] += 1
        char_count[ord(string2[i])-ord('a')] -= 1

    # print (char_count)
    for i in range(len(char_count)):
        if char_count[i] != 0:
            return False

    return True

def check_if_anagram_dic(string1,string2):
    n1 = len(string1)
    n2  = len(string2)
    if n1 != n2:
        return False

    char_count = {}

    for i in range(n1):
        if string1[i] in char_count.keys():
            char_count[string1[i]] += 1
        else:
            char_count[string1[i]] = 1
    
    for j in range(n2):
        char_count[string2[j]] -= 1


    # print (char_count)
    for k,v in char_count.items():
        if v != 0:
            return False

    return True
print(check_if_anagram_dic("silent","litens"))