class Stack:
    def __init__(self, size):
        self.value = [None]*size
        self.top = -1
        self.length = 0
        self.size = size

    def isEmpty(self):
        return self.length == 0 
   
    def isFull(self):
        return self.length == self.size

    def push(self, value):
        if self.isFull(): return "Stack is full"

        self.top+=1
        self.value[self.top] = value
        self.length+=1

    def pop(self):
        if self.isEmpty(): return "Stack is empty"
        removeNode = self.value[self.top]
        self.top -= 1
        self.length -= 1
        return removeNode
    
    def display(self):
        if self.isEmpty(): return "Stack is empty"
        for i in range(0, self.top+1):
            print(self.value[i])

s = Stack(5)
s.push(12)
s.push(2)
s.push(7)
s.push(11)
s.push(10)
print("remove element is ", s.pop())
print("remove element is ", s.pop())
print("remove element is ", s.pop())
print("remove element is ", s.pop())
print("remove element is ", s.pop())
print("remove element is ", s.pop())
