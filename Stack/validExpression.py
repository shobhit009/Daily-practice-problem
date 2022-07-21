#PS : Given a sequence of string of symbols. Determine whether a valid expression
# e.g - []{()} - Valid []]()} - Invalid

def getReverse(s,dic):
    if s in dic.keys():
        return dic[s]

def isLeftSymbol(s,list_):
    for ele in list_:
        if s == ele:
            return True
    

def isValidExpression(input_string):
    stack = []
    dic = {'[':']', '{' : '}', '(':')','}':'{',']':'[',')':'('}
    left_symbol_list = ['[','{','(']
    for s in input_string:  
        rev = getReverse(s,dic)     
        if isLeftSymbol(s,left_symbol_list):            
            stack.append(s)
        elif len(stack) == 0 or stack.pop() != rev:
            return False
    return (len(stack) == 0)


if __name__ == "__main__":
    input_string = "[]{()}[][][][][][][][][][][][][][][]})))))"
    result = isValidExpression(input_string)
    print (result)