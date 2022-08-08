class MinHeap:
    def __init__(self,s,c):
        self.arr=[0]*c
        self.size = 0
        self.capacity = c

    def left(self,i):
        return 2*i + 1

    def right(self,i):
        return 2*i + 2
    
    def parent(self,i):
        return (i-1)//2

    def insert(self,x):
        if self.size == self.capacity:
            return
        self.size += 1
        self.arr[self.size-1] = x

        for i in range(self.size):
            while (i != 0 and self.arr[self.parent(i)]>self.arr[i]):
                self.arr[self.parent(i)],self.arr[i] = self.arr[i],self.arr[self.parent(i)]
                i = self.parent(i)
                

    def print_value(self):
        for i in range(self.size):
            print(self.arr[i],sep=" ",end="|")
        
if __name__ == "__main__":
    minHeap = MinHeap(0,9)
    minHeap.insert(10)
    minHeap.insert(20)
    minHeap.insert(15)
    minHeap.insert(40)
    minHeap.insert(50)
    minHeap.insert(100)
    minHeap.insert(25)
    minHeap.insert(12)
    minHeap.print_value()
