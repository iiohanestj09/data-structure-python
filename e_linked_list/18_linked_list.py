class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        newNode = Node(value)
        if not self.head: self.head = newNode       # None = Falsy value, jadiii not None = True (cek head masih None atau tidak)
        else:                                       # objek apapun -> dianggap Truthy kalau tidak kosong
            last = self.head
            while last.next:           # loop hinga last.next bernilai None dan while akan berhenti
                last = last.next
            last.next = newNode
    
    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=" -> ")    # parameter end= akan menghapus newline default dari print() dan ngatur apa yg ditaruh setelah output
            current = current.next
        print("None")


# Implementasi
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.display()