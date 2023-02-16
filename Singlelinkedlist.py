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
    
    #Shift method adds node element to the front of the linkedlist
    def shift(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.next = newNode
            self.head = newNode
        self.length += 1
        return self
    
    #Unshift removes node element from the front of a linkedList
    def unshift(self):
        if self.head is None:
            print("This luinked list is empty")
            return
        current = self.head
        pre = self.head
        current.next = current
        pre = None
        self.length += 1
        return self
    
            
            