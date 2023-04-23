# The NODE Constructor

#A single linklist has head, tail, data and next
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self, value=None):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    #Push method adds a new node to the end of the linklist
    def push(self, data):
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
            return None
        pre = self.head
        current = self.head
        while current.next:
            pre = current
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
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self
    
    # Shift method removes node element from the front of the linkedlist
    def shift(self):
        if self.head is None:
            print("The linkedlist is empty")
        current = self.head.next
        self.head = current
        self.length -= 1
        if self.length == 1:
            self.tail = None
        return current
    
    #The get method helps to get a particular node
    def get(self, index):
        if index < 0 or index >= self.length:
            print("invalid")
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current

    # The set method help to set a particular data in place of another data
    def set(self, index, data):
        current = self.get(index)
        if current:
            current.data = data
            return True
        return False
    
    # The insert method is used to insert a particular node in a given space   
    # def insert(self, index, data):
    #     if index < 0 or index >= self.length:
    #         return False
    #     if index == self.length:
    #         return self.push(data)
    #     if index == 0:
    #         return self.unshift(data)
    #     newNode = Node(data)
    #     current = self.get(index - 1)
    #     newNode.next = current.next
    #     current.next = newNode
    #     self.length += 1
    #     return True
    
    # def remove(self,index):
    #     if index < 0 or index >= self.length:
    #         return False
    #     if index == self.length - 1:
    #         return self.pop()
    #     if index == 0:
    #         return self.shift()
    #     current = self.get(index - 1)
    #     current.next = current.next.next
    #     self.length -= 1
    #     return True
    
    # def delete_node(self, key):
    #     if self.head is None:
    #         print("Linked list is empty")
    #         return None
    #     if self.head.data == key:
    #         self.shift()
    #     if self.tail.data == key:
    #         self.pop()  
    #     current = self.head
    #     pre = None
    #     while current.next:
    #         if current.next.data == key:
    #             pre.next = current.next.next
    #             self.length -= 1
    #         else:
    #             pre = current
    #             current = current.next
    #     return self
    
    def reverse(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.tail
        self.tail = current
        pre = None
        for i in range(self.length):
            next = current.next
            current.next = pre
            pre = current
            current = next
        return self
    
    def __repr__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data) + " ---> "
            current = current.next
        return llstr     
    
     
     
#Days of the week
list = LinkedList("Sun")  
list.push("Mon")
list.push("Tue")
list.push("Wed")
list.push("Thur")
list.push("Fir")
list.push("Sat")
list.pop()
list.unshift("Sat")
list.shift()
print(list.get(1))
# list.set(0,"Sun")
list.insert(0, "Wed")
list.remove(2)
list.delete_node("Thur")
list.reverse()
print(list)
    
        
            
    
   
    
            
            