class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)         # O(1) amortized, kadang O(1) kadang O(n) karena resize list
    
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
        else: print(f"{self.items[::-1]}")     # list[start:stop:step]


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