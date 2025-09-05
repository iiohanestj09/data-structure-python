# Graph dengan Adjacency Matrix versi directed dan weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def addEdge(self, src, dest, weight):
        if src < self.vertices or dest < self.vertices:
            self.adjMatrix[src][dest] = weight
        else: print(f"Error: {src} atau {dest} tidak ditemukan!")
    
    def removeEdge(self, src, dest):
        if src < self.vertices and dest < self.vertices:
            self.adjMatrix[src][dest] = 0
        else: print(f"Error: {src} atau {dest} tidak ditemukan!")
    
    def display(self):
        print("   " + " ".join(str(i) for i in range(self.vertices)))
        
        for i in range(self.vertices):
            print(f"{i}| " + " ".join(str(j) for j in self.adjMatrix[i]))
            

# Implementasi
gr = Graph(5)

gr.addEdge(0, 1, 3)
gr.addEdge(0, 3, 2)
gr.addEdge(0, 4, 6)
gr.addEdge(1, 0, 8)
gr.addEdge(1, 2, 9)
gr.addEdge(1, 4, 2)
gr.addEdge(2, 0, 3)
gr.addEdge(2, 1, 1)
gr.addEdge(2, 4, 4)
gr.addEdge(3, 0, 1)
gr.addEdge(3, 2, 6)
gr.addEdge(3, 4, 8)
gr.addEdge(4, 0, 3)
gr.addEdge(4, 1, 6)
gr.addEdge(4, 2, 7)
gr.addEdge(4, 3, 4)

gr.removeEdge(0, 4)
gr.removeEdge(1, 0)
gr.removeEdge(2, 1)
gr.removeEdge(3, 2)

gr.display()

#    0 1 2 3 4
# 0| 0 3 0 2 0 
# 1| 0 0 9 0 2
# 2| 3 0 0 0 4
# 3| 1 0 0 0 8
# 4| 3 6 7 4 0            