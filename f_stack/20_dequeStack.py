# Menggunakan collections.deque  -> lebih efisien daripada listStack
# Segi big o notation, deque() lebih efisien dari list utk membuat stack

from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
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
        else: print(list(reversed(self.items)))


# Implementation
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