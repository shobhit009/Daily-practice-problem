


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:

    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        node = Node(data)
        if self.head:
             node.next = self.head
             self.head = node
        self.head =node
       

    def insertAfter(self,previousNodeValue,data):
        node = Node(data)
        temp = self.head
        while (temp.data != previousNodeValue):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def append(self,data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def delete(self,data):
        curr = self.head
        while curr.data != data:
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr = None

    def Print(self):
        temp = self.head
        while temp:            
            print(temp.data)
            temp = temp.next
    

if __name__ == "__main__":
    # nodeA = Node(8)
    ll = LL()
    ll.insertAtBegining(4)
    ll.insertAtBegining(3)
    ll.insertAfter(4,5)
    ll.insertAfter(4,6)
    ll.append(7)
    ll.delete(4)
    ll.delete(7)
    ll.Print()




