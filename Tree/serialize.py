class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def serialize_bt(root, x):
    if root is None:
        x.append(-1)
        return 

    x.append(root.data) 
    serialize_bt(root.left,x)
    serialize_bt(root.right,x)
    return x

def deserialize_bt(arr):
    global idx
    if idx == len(arr):
        return
    
    val = arr[idx]
    idx +=1
    if val == -1:
        return None
    
    root = Node(val)
    root.left = deserialize_bt(arr)
    root.right = deserialize_bt(arr)
    return root
        


if __name__=="__main__":

    idx = 0
    x = []
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
    serialized_array = serialize_bt(root,x)
    print (deserialize_bt(serialized_array).data)