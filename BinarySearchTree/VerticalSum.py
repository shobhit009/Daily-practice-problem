class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def verticalSum(root,hd,Map):
    if root is None:
        return 
    verticalSum(root.left,hd-1,Map)
    if (hd in Map.keys()):
        Map[hd] += root.data
    else:
        Map[hd] = root.data

    verticalSum(root.right,hd+1,Map)     
    


def verticalSumWrapper(root):
    Map = {}
    verticalSum(root,0,Map)
    for k in sorted(Map.keys()):
        print (Map[k])

if __name__ =="__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(50)
    root.left.left = Node(30) 
    root.left.right = Node(40)
    verticalSumWrapper(root)