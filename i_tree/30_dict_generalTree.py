# General Tree dengan implementasi dictionary

class Tree:
    def __init__(self):
        self.tree = {}      # {parent: [children]}  {string: List->[string]}
    
    def addNode(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        self.tree[parent].append(child)
    
    def removeNode(self, parent, child):
        if parent in self.tree and child in self.tree[parent]:
            self.tree[parent].remove(child)
    
    def display(self, node, level=0):
        print("  " * level + str(node))
        if node in self.tree:
            for child in self.tree[node]:
                self.display(child, level + 1)


# Implementasi
gTree = Tree()

# Tambah anak ke root
gTree.addNode("A", "B")
gTree.addNode("A", "C")
gTree.addNode("A", "D")

# Tambah anak ke B
gTree.addNode("B", "E")
gTree.addNode("B", "F")

# Tambah anak ke node C
gTree.addNode("C", "G")

# Tambah anak ke node G
gTree.addNode("G", "H")

gTree.display("A")

"""
Output:
A
  B    
    E  
    F  
  C    
    G  
      H
  D  
"""