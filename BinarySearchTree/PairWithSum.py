import sys
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isPair(root,target,s):
    if root is None:
        return False
    
    if isPair(root.left,target,s)  == True:
        return True

    if target-root.data in s:
        return True
    else:
        s.append(root.data)
    
    return isPair(root.right,target,s)

if __name__ =="__main__":
    s = []
    root = Node(20)
    root.left = Node(8)
    root.right = Node(30)
    root.right.left = Node(18) 
    root.right.right = Node(35)
    print (isPair(root,100,s))