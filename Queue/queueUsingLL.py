class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        
        if self.head == self.tail == None:
            self.head = newNode
            self.tail = self.head
        
        else:
            self.tail.next = newNode
            self.tail = newNode


    def dequeue(self):
        temp = self.head
        if self.head is not None:
            self.head = self.head.next
            temp = None


    def print(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    def peek(self):
        print (self.head.data)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.peek()
    queue.print()
    queue.dequeue()
    queue.print()