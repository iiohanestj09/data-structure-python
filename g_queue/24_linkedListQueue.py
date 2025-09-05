class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.frontNode = None
        self.rearNode = None
        self.size = 0
        
    def enqueue(self, value):
        newNode = Node(value)
        
        if self.isEmpty(): self.frontNode = self.rearNode = newNode
        else:
            self.rearNode.next = newNode
            self.rearNode = newNode
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Gagal dequeue, Queue kosong!")
            return None
        
        removedValue = self.frontNode.data
        self.frontNode = self.frontNode.next
        
        if self.isEmpty(): self.rearNode = None
        
        self.size -= 1
        return removedValue
    
    def front(self):    
        if self.isEmpty():
            print("Gagal front, Queue kosong!")
            return None
        return self.frontNode.data
        
    def isEmpty(self):
        return self.frontNode is None    
    
    def display(self):
        if self.isEmpty(): print("Gagal display, Queue kosong!")
        else:
            current = self.frontNode
            while current:
                print(current.data, end=" <- ")
                current = current.next
            print("None")            
        
# Implementasi
que = Queue()

que.dequeue()
que.display()

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)

print(que.dequeue())
que.enqueue(40)

print(f"front:", que.front())
que.display()        