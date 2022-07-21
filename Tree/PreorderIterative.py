class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder_iterative(root):
    s = []
    curr = root

    while (curr is not None or len(s) > 0):
        while (curr is not None):
            print (curr.data)
            s.append(curr)
            curr = curr.left

        curr = s.pop()
        if curr.right is not None:
            curr = curr.right
        else:
            curr = None    

if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.left.left.left = Node(70)
    root.left.left.right = Node(80)
    root.right = Node(30)
    root.right.left = Node(60)
    # root.right.left.left = Node(60)
    # root.right.right = Node(70)
    preorder_iterative(root)