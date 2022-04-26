# URLify: Write a method to replace all spaces in a string with '%20'. 
# you may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. 


def URLify(string, length) -> str:
    #Trim left and right spaces

    if length < 0:
        return "Invalid String"
    trimmed_string = string.strip()
    output_string = trimmed_string.replace(" ", "%20")
    return output_string


if __name__ == "__main__":
    print(URLify("Mr John Smith ",13))