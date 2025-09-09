# Menggunakan collections.deque  -> lebih efisien daripada listStack
# Segi big o notation, deque() lebih efisien dari list utk membuat stack

from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        self.items.append(item)     # Selalu O(1) operation, karena saat saat nambah cukup bikin pointer baru
    
    def pop(self):
        if self.isEmpty():
            print("Gagal pop, Stack kosong!")
            return None
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty(): 
            print("Gagal peek, Stack kosong!")
            return None
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
        
    def display(self):
        if self.isEmpty(): print("Gagal display, Stack kosong!")
        else: print(list(reversed(self.items)))


# Implementasi
st = Stack()

print(st.pop())
st.display()

st.push(10)
st.push(20)
st.push(30)

print(st.pop())
st.push(40)

print("Peek:", st.peek())
st.display()