class CircularQueue:

    def __init__(self,cap):
        self.data = list()
        self.capacity = cap
        self.size = 0
        self.front = 0

    def enqueue(self,target): 
        self.data.append(target)
        self.size += 1

    def dequeue(self):
        temp = self.data[self.front]
        self.data.pop(self.front)
        self.size -= 1
        return temp

    def display(self):
        bantuList = []
        
        for theData in self.data:
            if theData != None:
                bantuList.append(theData)
        
        print('Yang ada pada antrian adalah: ',end=' ')
        for data in bantuList:
            print(data,end=' ')
        print()

CircularQueue = CircularQueue(5)
CircularQueue.enqueue(14)
CircularQueue.enqueue(22)
CircularQueue.enqueue(13)
CircularQueue.enqueue(-6)
CircularQueue.display()
print('Data yang dihapus adalah = ', CircularQueue.dequeue())
print('Data yang dihapus adalah = ', CircularQueue.dequeue())
CircularQueue.display()
CircularQueue.enqueue(9)
CircularQueue.enqueue(20)
CircularQueue.enqueue(5)
CircularQueue.display()