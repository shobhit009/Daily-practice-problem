# Assumption - We will always burn from leaf
# Hint - For each node , we will compute it's height and distance from the given leaf node

class Distance:
    def __init__(self,d):
        self.val = d
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def burnTime(root, leafNode, dist):
    global res
    if root is None:
        return 0

    if (root.data == leafNode):
        dist.val = 0
        return 1
    ldist = Distance(-1)
    rdist = Distance(-1)
    lh = burnTime(root.left, leafNode, ldist)
    rh = burnTime (root.right, leafNode, rdist)

    if (ldist.val!=-1):
        dist.val = ldist.val + 1
        res = max(res, dist.val + rh)
    elif (rdist.val != -1):
        dist.val = rdist.val + 1
        res = max(res, dist.val + lh)
    
    return max(lh,rh) + 1



if __name__=="__main__":

    res = 0
    root = Node(10)
    root.left = Node(40)
    root.right = Node(50)
    root.right.left = Node(60)
    root.right.left.left = Node(80)
    root.right.left.right = Node(90)
    root.right.left.right.left = Node(100)
    root.right.right = Node(70)
    dist = Distance(-1)
    burnTime(root,40,dist)
    print(res)