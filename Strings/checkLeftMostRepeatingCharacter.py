# Alphabetically first letter occuring more than one time


def alphabetically_most_repeating_character(string):
    n = len(string)
    frequency = [0]*26

    for i  in range(n):
      frequency[ord(string[i])-ord('a')] += 1

    for i in range(len(frequency)):
        if frequency[i] > 1:
            break

    return chr(i+ord('a'))

# print(alphabetically_most_repeating_character("geeksforgeeks"))

#Method 2
def left_most_repeating_character(string):
    n = len(string)
    frequency = {}

    for c in string:
        if c in frequency.keys():
            frequency[c] += 1

        else:
            frequency[c] = 1

    for k,v in frequency.items():
        if v > 1:
            for j in range(n):
                if string[j] == k:
                    return j

    return -1  

#Method 3 - Storing index and count of a character as list {"a":[0,1]}
def left_most_repeating_character_imp(string):
    n = len(string)
    frequency = {}

    for i in range(len(string)):
        if string[i] in frequency.keys():
            frequency[string[i]][1] += 1

        else:
            frequency[string[i]] = [i,1]

    for v in frequency.values():
        if v[1] > 1:
            return v[0]  
    return -1
print(left_most_repeating_character_imp("geeksforgeeks"))



