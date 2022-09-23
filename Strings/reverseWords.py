def reverseWords(string):
    list_of_words = list(string.split(" "))
    return " ".join(list_of_words[::-1])
# print (reverseWords("I Love Coding"))

def reverse_word(string):
    n = len(string)
    start = 0
    for i in range(n):
        if string[i] == " ":
            reverse(string,start,i)
            start = i + 1
    reverse(string,start,n-1)
    reverse (string,0,n-1)
    return string

def reverse(string,start,end):
    while (start <= end):
        string[start],string[end] = string[end], string[start]
        start += 1
        end -= 1

print (reverse_word("I Love Coding"))   

