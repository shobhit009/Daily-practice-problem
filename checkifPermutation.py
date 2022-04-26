# check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.
# Runtime : O(n), Space : O(n)

from xmlrpc.client import Boolean

# Approach 1 -  Using two dictionary 
# def checkPermutation(origString,stringTobeChecked)->Boolean:
#     if (len(origString) != len(stringTobeChecked)):
#         return False
    
#     origString_dic ={}
#     stringTobeChecked_dic ={}

#     createDictionary(origString_dic,origString)
#     createDictionary(stringTobeChecked_dic,stringTobeChecked)
    
#     for char,count in stringTobeChecked_dic.items():
#         if ((char not in origString_dic.keys()) or (origString_dic[char] != count)):
#             return False
#     return True  

# def createDictionary(dictionary, string) -> None:
#     for char in string.lower():
#         if char in dictionary.keys():
#             dictionary[char] += 1
#         else:
#             dictionary[char] = 0        
#     return None

# if __name__ == "__main__":
#     print(checkPermutation("shobhit","HOBHITS"))


#Approach 2- Using Single dictionary

def checkPermutation(origString,stringTobeChecked)->Boolean:
    if (len(origString) != len(stringTobeChecked)):
        return False
    
    origString_dic ={}
    # stringTobeChecked_dic ={}

    createDictionary(origString_dic,origString)
    
    
    for char in stringTobeChecked.lower():
        if ((char not in origString_dic.keys())):
            return False
        else:
            origString_dic[char] -= 1
            if(origString_dic[char]< 0):
             return False   
    return True  

def createDictionary(dictionary, string) -> None:
    for char in string.lower():
        if char in dictionary.keys():
            dictionary[char] += 1
        else:
            dictionary[char] = 1        
    return None

if __name__ == "__main__":
    print(checkPermutation("shobhit","HOOBHITS"))