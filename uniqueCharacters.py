from xmlrpc.client import boolean


def uniqueCharacters(input_string)->boolean:
    dict = {}
    for char in input_string:
        if char in dict.keys():
            dict[char] += 1
            return False
        else:
            dict[char] = 0

    return True


if __name__ == "__main__":
    print (uniqueCharacters("aaa"))