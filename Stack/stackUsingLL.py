
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head is not None:  
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            print("Nothing to pop")    

    def top(self):
        print (self.head.data )   

    def print(self):
        while(self.head):
            print (self.head.data,end="->")
            self.head = self.head.next

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(5)
    # stack.top()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(8)
    stack.print()