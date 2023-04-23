class Node:
    def __init__(self, value=None, next=None):
        self.value= value
        self.next = next
        
class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.length = 1
        
    def printStack(self):
        current = self.top
        while current:
           print(current.value)
           current = current.next
    
    def getTop(self):
        if self.top is None:
           print("Top: null")
        else:
           print("Top: " + str(self.top.value))

    def getLength(self):
        print("Length: " + self.length)
           
    def makeEmpty(self):
        self.top = None
        self.length = 0
        
    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
            return
        newNode.next = self.top
        self.top = newNode
        self.length += 1
        return self
    
    def pop(self):
        if self.top is None:
            return None
        self.top = self.top.next
        self.length -= 1
        return self
    
    
myStack = Stack(2)
myStack.push(1)
myStack.push(3)
myStack.push(4)
myStack.push(6)
myStack.pop()
myStack.getTop()
myStack.printStack()