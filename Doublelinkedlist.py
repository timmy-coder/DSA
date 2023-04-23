class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        
class DoubleLinkedList:
    def __init__(self, value=None):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        if value:
            self.length = 1
        else:
            self.length = 0
        
    def push(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1
        return self
    
    def pop(self):
        if self.head is None:
            print("Linkedlist is empty")
            return None
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.length -= 1
        
    def Unshift(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self
        
    def shift(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        self.head.next.prev = None
        self.head = self.head.next
        self.lenght -= 1
        if self.length == 1:
            self.tail = None
        return self
    
    def get(self, index):
        if index < 0 or index >= self.length:
            print("invalid")
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current
    
    def set(self, index, value):
        current = self.get(index)
        if current:
            current.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Invalid")
            return None
        if index == 0:
            return self.Unshift(value)
        if index == self.length:
            return self.push(value)
        newNode = Node(value)
        current = self.get(index- 1)
        current.next.prev = newNode
        newNode.next = current.next
        newNode.prev = current
        current.next = newNode
        self.length += 1
        return self
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Invalid Index") 
            return None
        if index == 0:
            return self.shift()
        if index == self.length-1:
            return self.pop()
        current = self.get(index - 1)
        current.next = current.next.next
        current.next.prev = current
        self.length -= 1
        return self
    
    def delete_node(self, key):
        if self.head is None:
            print("Linked list is empty")
            return None
        if self.head.value == key:
            self.shift()
        if self.tail.value == key:
            self.pop()  
        current = self.head
        while current.next:
            if current.next.value == key:
                current.next.prev = current.next.next
                current.next.prev = current
                self.length -= 1    
            else:
                current = current.next
        return self
                  
    def reverse(self):
        if self.head is None:
            return None
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return self
                
    def __str__(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        output = ""
        while current:
            output += str(current.value) + " <-> "
            current = current.next
        return output
        

        

list = DoubleLinkedList("1")
list.push("2")
list.push("3")
list.push("4")
list.push("5")
list.insert(3, "10")
list.remove(3)
list.delete_node("2")
print(str(list))

