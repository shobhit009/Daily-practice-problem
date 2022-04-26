# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

def compressString(string)->str:

    n = len(string)
    countConsecutive = 0
    if n<=0:
        return False
    resultString = ""
    for i in range(n-1):
        countConsecutive += 1

        if (i+1>n or string[i] != string[i+1]):
            resultString  += "" + string[i]+ str(countConsecutive)
            countConsecutive = 0
    return resultString if len(resultString)<n else string

if __name__ == "__main__":
    print (compressString("aabcccccaaa"))