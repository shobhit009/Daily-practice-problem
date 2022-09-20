# count frequency of character in order

def count_frequency(string):
    freq = [0]*26

    for c in string:
        freq[ord(c)-ord('a')] += 1
    
    # print (freq)

    for i in range(len(freq)):
        if freq[i] > 0:
            print (chr(i+ord('a')),freq[i])

count_frequency('geeksforgeeks')