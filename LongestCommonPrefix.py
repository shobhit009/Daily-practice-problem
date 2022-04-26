# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl


def longestCommonPrefix(stringList)->str:

    if(not stringList):
        return ""

#sort string list in-laceon length
    stringList.sort(key = len)
    firstString = stringList[0]

    for i,c in enumerate(firstString):
        for string in stringList[1:] :
            if (string[i] != c):
                return firstString[:i]

    return firstString

if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))

