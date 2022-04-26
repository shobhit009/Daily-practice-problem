# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false

from xmlrpc.client import Boolean


def getDifferenceCount (str1, str2, count) -> int:
    for char in str1:
        if (char in str2) :
            count += 1
    return count        


def isOneAway(referenceString, modifiedString)-> Boolean:

    if (len(referenceString)<=0 or len(modifiedString)<=0):
        return False

    sorted_reference_string = sorted(referenceString)
    sorted_modified_string = sorted(modifiedString)
    count = 0
    #Base case
    
    # Case1: remove
    if (len(referenceString)-len(modifiedString) == 1):
        count = getDifferenceCount(sorted_modified_string,sorted_reference_string,count)            
        if count == len(modifiedString):
            return True
          

    # Case 2: insert 
    if (len(modifiedString)-len(referenceString) == 1):
        count = getDifferenceCount(sorted_reference_string,sorted_modified_string,count)
        if count == len(referenceString):
            return True

    # Case3 : replace
    if (len(modifiedString) == len(referenceString)):
        count = getDifferenceCount(sorted_modified_string,sorted_reference_string,count)               
        if (len(referenceString) - count)== 1:
            return True

    return False


if __name__ == "__main__":
    print (isOneAway("pale","pal"))