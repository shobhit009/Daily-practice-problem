class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BottomView(root):
    if root is None:
        return 

    q = []
    mp = {}
    q.append([root,0])

    while (len(q)):
        curr = q[0][0]
        hd = q[0][1]
        q.pop(0)

        if hd in sorted(mp):
            mp[hd] = curr.data
        else:
            mp[hd] = curr.data

        if (curr.left):
            q.append([curr.left, hd-1]) 
        if (curr.right):
            q.append([curr.right, hd+1])    

    for k in sorted(mp.keys()):
        print (mp[k]) 

if __name__ =="__main__":
    root = Node(10)
    # root.left = Node(20)
    # root.right = Node(30)
    # root.left.left = Node(40) 
    # root.left.right = Node(50)

    root.left = Node(20)
    root.right = Node(30)
    root.left.right = Node(50) 
    root.left.right.right = Node(60)
    BottomView(root)