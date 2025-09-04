class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            print("Gagal dequeue, Queue is empty!")
            return None
        return self.items.pop(0)        # hapus item terdepan
    
    def front(self):
        if self.isEmpty():
            print("Gagal front, Queue is empty!")
            return None
        return self.items[0]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def display(self):
        if self.isEmpty(): print("Gagal display, Queue is empty!")
        else: 
            print(self.items)
            

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