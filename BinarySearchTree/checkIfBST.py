import sys
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root,prev):
    if root is None:
        return True
    
    if isBST(root.left,prev)  == False:
        return False

    if (root.data<=prev):
        return False
    
    prev = root.data
    return isBST(root.right,prev)

if __name__ =="__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(30)
    root.right.left = Node(18) 
    root.right.right = Node(35)
    print (isBST(root,-sys.maxsize-1))