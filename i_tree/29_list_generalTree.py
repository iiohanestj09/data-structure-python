# General TreeNode dengan implementasi List

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def addChild(self, childNode):
        self.children.append(childNode)
        
    def removeChild(self, childValue):
        self.children = [child for child in self.children if child.value != childValue]
        
    def display(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)


# Implementasi
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

# Tambah anak ke root
root.addChild(b)
root.addChild(c)
root.addChild(d)

# Tambah anak ke node B
b.addChild(TreeNode("E"))
b.addChild(TreeNode("F"))

# Tambah anak ke node C
g = TreeNode("G")
c.addChild(g)

# Tambah anak ke node G
g.addChild(TreeNode("H"))

root.display()

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