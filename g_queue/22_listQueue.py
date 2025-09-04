class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)         # O(1) amortized
    
    def dequeue(self):
        if self.isEmpty():
            print("Gagal dequeue, Queue kosong!")
            return None
        return self.items.pop(0)        # O(n), hapus item terdepan dan semuanya bergeser ke kiri
    
    def front(self):
        if self.isEmpty():
            print("Gagal front, Queue kosong!")
            return None
        return self.items[0]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def display(self):
        if self.isEmpty(): print("Gagal display, Queue kosong!")
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