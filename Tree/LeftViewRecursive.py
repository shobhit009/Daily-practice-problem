class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root,level):

    ## pre-order traversal
    global maxlevel
    if root is None:
        return 

    if maxlevel < level:
        print (root.data)
        maxlevel = level
    
    if root.left is not None:
        leftView(root.left, level+1)
    if root.right is not None:
        leftView(root.right, level+1)

if __name__=="__main__":

    maxlevel = 0
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    leftView(root,1)




