# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.) 


from xmlrpc.client import Boolean


def isPalindromePermutation(string)->Boolean:
    oddCount = 0
    if len(string) <= 0:
        return False
    dic ={}
    for char in string.strip():
        if char not in dic.keys():
            dic[char] = 1
        else:
            dic[char] += 1      
# if string length is even , then there can;t be any charcter with odd count and if string length is odd then there can be atmost one character 
# with oddcount
    for item in dic.keys():
        if ((dic[item] % 2 == 1)):
            oddCount +=1

    return (oddCount <=1)


if __name__ == "__main__":
    print(isPalindromePermutation("abzxzab"))