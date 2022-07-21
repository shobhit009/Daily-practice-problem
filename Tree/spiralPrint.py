class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def spiral(root):
    if root is None:
        return
    q = []
    s = []
    q.append(root)
    reverseFlag = False
    while(len(q)>0):
        temp = len(q)
        for i in range(temp):    
            curr = q.pop(0)

            if reverseFlag:
                s.append(curr.data)
            else:
                print (curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        if (reverseFlag):
            while(len(s)>0):
                print(s.pop())

        reverseFlag = not(reverseFlag)
if __name__=="__main__":

 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    spiral(root)