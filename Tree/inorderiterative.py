


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_iterative(root):
    s = []
    curr = root

    while (curr is not None or len(s) > 0):
        while (curr is not None):
            s.append(curr)
            curr = curr.left

        curr = s.pop()
        print (curr.data)
        curr = curr.right

if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    inorder_iterative(root)
