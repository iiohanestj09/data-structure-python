# Menggunakan collections.deque  -> lebih efisien daripada listQueue
# Segi big o notation, deque() lebih efisien dari list utk membuat queue

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.isEmpty():
            print("Gagal dequeue, Queue kosong!")
            return None
        return self.items.popleft()     # 0(1) karena tinggal putus pointer di front
    
    def front(self):
        if self.isEmpty():
            print("Gagal front, Queue kosong!")
            return None
        return self.items[0]
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def display(self):
        if self.isEmpty(): print("Gagal display, Queue kosong!")
        else: print(list(self.items))
        

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