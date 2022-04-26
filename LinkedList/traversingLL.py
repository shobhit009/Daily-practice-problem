
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtBegining(self,data):
        newNode = Node(data)

        if (self.head):
            newNode.next = self.head
            self.head = newNode
        
        self.head = newNode

    def insertAfter(self, previousNodeData, data):
        newNode = Node(data)
        temp = self.head
        while(temp.data == previousNodeData):
            temp = temp.next
        newNode.next = temp.next.next
        temp.next.next = newNode

    def appendAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while (temp.next):
            temp = temp.next
        
        temp.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    ## instantiating an empty linked list

    ll = LinkedList()
    # ll.head = Node(1)
    # secondNode =  Node(2)
    # thirdNode = Node(3)

    # ll.head.next = secondNode
    # secondNode.next = thirdNode

    ll.insertAtBegining(4)
    ll.insertAtBegining(3)
    ll.appendAtEnd(5)
    ll.insertAfter(4,6)
    ll.printList()
