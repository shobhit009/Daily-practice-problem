

#Method 3 - Storing index and count of a character as list {"a":[0,1]}
def left_most_non_repeating_character(string):
    n = len(string)
    frequency = {}

    for i in range(len(string)):
        if string[i] in frequency.keys():
            frequency[string[i]][1] += 1

        else:
            frequency[string[i]] = [i,1]

    for v in frequency.values():
        if v[1] < 2:
            return v[0]  
    return -1
print(left_most_non_repeating_character("abbcbda"))



