class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None
        poppedValue = self.top.data
        self.top = self.top.next
        self.size -= 1
        return poppedValue
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None
        return self.top.data    
    
    def isEmpty(self):
        return self.top is None
    
    def display(self):
        if self.isEmpty(): print("Stack is empty!")
        else:
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


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
     