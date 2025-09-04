class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty!")
            return None
        return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty!")
            return None
        return self.items[-1]
    
    def display(self):
        if len(self.items) == 0: print("Stack is empty!")
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