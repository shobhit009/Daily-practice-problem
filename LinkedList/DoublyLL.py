class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:

    def __init__(self):
        self.head = None


    def insertAtBegining(self,data):
        node = Node(data)
        node.next = self.head
        if (self.head is not None):
            self.head.prev = node
        
        self.head = node

    def insertAfter(self,prevValue,data):
        newNode = Node(data)
        temp = self.head

        while(temp.data != prevValue):
            temp = temp.next
        
        newNode.next = temp.next
        temp.next = newNode

        if newNode.next is not None:
            newNode.next.prev = newNode
        newNode.prev = temp

    def insertBefore(self, afterValue, data):
        newNode = Node(data)
        temp = self.head
        while (temp.data != afterValue):
            temp = temp.next
        newNode.prev = temp.prev
        temp.prev = newNode
    
        if newNode.prev is not None:
            newNode.next = newNode.prev.next
            newNode.prev.next = newNode

    def append(self, data):
        newNode = Node(data)
        last = self.head

        if(last is not None):
            while (last.next):
                last = last.next
            last.next = newNode
            newNode.prev = last

        last = newNode

    
    def delete(self,val):

        temp = self.head       
        if self.head is None:
            return

        # if key is at first node of DLL having more than one node 3->5->
        if (temp.data == val):
            if (temp.next is not None ):
                self.head = self.head.next
                self.head.prev = None
            else:   #DLL has just one node 
                temp = None
                self.head = None
            return

        # if key is in somewhere middle

        while(temp):
            if (temp.data == val):
                if temp.next is not None :
                     temp.next.prev = temp.prev
                     temp.prev.next = temp.next
                     temp = None
        #  key is at last             
                else:     
                    temp.prev.next = None     
                    temp.prev = None
                    temp = None
                return
            temp = temp.next
        print ("key not found")
       
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

if __name__ == "__main__":
    dl = DLL()
    dl.insertAtBegining(4)
    dl.insertAtBegining(3)
    dl.insertAfter(3,5)
    dl.insertBefore(4,8)
    dl.insertBefore(8,9)   
    dl.append(30)
    dl.delete(3)
    dl.insertAtBegining(12)
    dl.delete(8)
    dl.delete(30)
    dl.delete(48)
    dl.printList()