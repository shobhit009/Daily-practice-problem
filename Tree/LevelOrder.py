

class Node:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None


def printlevelorder(root):
    queue = []
    queue.append(root)
    while (len(queue)):
        curr = queue.pop(0)
        print(curr.data)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:   
            queue.append(curr.right)


if __name__ =="__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(8)
    root.left.right = Node(7)
    root.right.right = Node(30)
    printlevelorder(root)


