#Assumption:
# Both keys are present in Binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLCA(root, n1, n2):
    if root is None:
        return None

    if (root.data == n1 or root.data == n2):
        return root

    lca1 = isLCA(root.left,n1,n2)
    lca2 = isLCA(root.right,n1,n2)

    if (lca1 is not None and lca2 is not None):
        return root

    if (lca1 is not None):
        return lca1
    else:
        return lca2


if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    print(isLCA(root,40,30).data)