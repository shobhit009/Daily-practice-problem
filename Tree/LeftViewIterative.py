class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root):
    if root is None:
        return
    q = []
    q.append(root)
    while(len(q)>0):
        temp = len(q)
        for i in range(temp):
            curr = q.pop(0)
            if i == 0:
                print (curr.data)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    LeftView(root)
