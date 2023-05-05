class Queue:
    def __init__(self,size):
        self.value = [None]*size
        self.front = -1
        self.rear = -1
        self.length = 0
        self.size = size
    
    def isEmpty(self):
        return self.length == 0
    
    def isFull(self):
        return self.length == self.size
    
    def enqueue(self, value):
        if self.isFull(): return "Queue is full"
        if self.isEmpty():
            self.front+=1
            self.rear+=1
            self.value[self.rear] = value
        else:
            self.rear+=1
            self.value[self.rear] = value
        
        self.length+=1

    def dequeue(self):
        if self.isEmpty(): return "Queue is empty"
        removedNode = None
        if self.length==1:
            removedNode = self.value[self.front]
            self.value[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            removedNode = self.value[self.front]
            self.value[self.front] = None
            self.front += 1
        self.length-=1
        return removedNode
    
    def display(self):
        if self.isEmpty(): return "Queue is empty"
        for i in range(self.front, self.rear+1):
            print("element is", self.value[i])
    
q = Queue(5)
q.enqueue(3)
q.enqueue(13)
q.enqueue(2)
q.enqueue(6)
q.enqueue(7)
print("remove element", q.dequeue())
print("remove element", q.dequeue())
print("remove element", q.dequeue())
print("remove element", q.dequeue())
print("remove element", q.dequeue())
print("remove element", q.dequeue())
q.display()
