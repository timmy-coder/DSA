# The NODE Constructor

#A single linklist has head, tail, data and next
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    #Push method adds a new node to the end of the linklist
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    
    # Pop method removes the last node from the end of the linkedlist
    def pop(self):
        if self.head is None:
            print('This linklist is empty')
            return
        current = self.head
        pre = self.head
        while current.next:
            current = pre
            current = current.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None 
            self.tail = None
        return current
    
    #Unshift method adds node element to the front of the linkedlist
    def unshift(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.next = newNode
            self.head = newNode
        self.length += 1
        return self
    
    # Shift method removes node element from the front of the linkedlisy
    def shift(self):
        if self.head is None:
            print("The linkedlist is empty")
        current = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 1:
            self.tail = None
        #current.next = None
        return current
    
    #The get method helps to get a particular node
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current
    
    # The set method help to set a particular data in place of another data
    def set(self,index, data):
        current = self.get(index)
        if current:
            current.data = data
            return True
        return False
        
        
    # The insert method is used to insert a particular node in a given space
    
    def insert(self, index, data):
        if index < 0 or index >= self.length:
            return False
        if index == self.length:
            return self.pop(data)
        if index == 0:
            return self.unshift(data)
    
        newNode = Node(data)
        current = self.get(index -1)
        current.next = newNode
        current.next = newNode.next
        self.length += 1
        return True
    
        
    
        
            
    
   
    
            
            