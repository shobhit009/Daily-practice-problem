from re import I
from turtle import left


class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def CBT(ino,po,ist,ie)->TreeNode:
    if (ist > ie):
        return None

    global postIndex
    inIndex  = 0
    root = TreeNode(po[postIndex])
    postIndex -= 1

    if (ist == ie):
        return root
    
    for i in range(ist,ie):
        if ino[i] == root.data:
            inIndex = i
            break

    root.right = CBT(ino,po,inIndex+1,ie)
    root.left = CBT(ino,po,ist,inIndex-1)

    return root

def printPreorder(node):
    if node is None:
        return
     
    # then print the data of node
    print (node.data,end=' ')
    # first recur on left child
    printPreorder(node.left)   
  
 
    # now recur on right child
    printPreorder(node.right)

def printPostorder(node):
    if node is None:
        return
     
   
    # first recur on left child
    printPostorder(node.left)   
  
 
    # now recur on right child
    printPostorder(node.right)

     # then print the data of node
    print (node.data,end=' ')
if __name__ == "__main__":
    ino = [30,20,10,50,40,60]
    po = [30,20,50,60,40,10]
    postIndex = len(po)-1
    ie = len(ino)-1
    root = CBT(ino,po,0,ie)
    printPreorder(root)
    print("\n")
    print(root.data)
    print("\n")
    printPostorder(root)

