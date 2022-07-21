class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPath(root,p,key):
    if root is None:
        return False
    
    p.append(root.data)
    if root.data == key:
        return True

    if (findPath(root.left,p,key) or findPath(root.right, p, key)):
        return True
    
    p.pop(len(p)-1)

    return False
    

def isLca(root,n1,n2):
    path1 = []
    path2 = []
    if (findPath(root,path1,n1) == False or findPath(root,path2,n2) == False):
        return None
    
    smallest = len(path2) if len(path1)>len(path2) else len(path1)
    for i in range(smallest):
        if path1[i+1] != path2[i+1]:
            return path1[i]
    

if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    print(isLca(root,40,50))

    ##Time Complexity - Theta(n) - 3 binary tree traversals