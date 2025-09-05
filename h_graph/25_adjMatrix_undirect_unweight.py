# Graph dengan Adjacency Matrix versi undirected dan unweighted

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def addEdge(self, v1, v2):
        if v1 < self.vertices and v2 < self.vertices:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
        else: print(f"Error: {v1} atau {v2} tidak ditemukan!")
    
    def removeEdge(self, v1, v2):
        if v1 < self.vertices and v2 < self.vertices:
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0
        else: print(f"Error: {v1} atau {v2} tidak ditemukan!")
    
    def display(self):
        print("   " + " ".join(str(i) for i in range(self.vertices)))
        
        for i in range(self.vertices):
            print(f"{i}| {" ".join(str(j) for j in self.adjMatrix[i])}")


# Implementasi
gr = Graph(5)

gr.addEdge(0, 1)
gr.addEdge(3, 4)
gr.addEdge(2, 2)
gr.addEdge(2, 1)
gr.addEdge(4, 1)
gr.addEdge(3, 2)
gr.addEdge(4, 4)
gr.addEdge(0, 3)

gr.removeEdge(0, 1)
gr.removeEdge(2, 2)
gr.removeEdge(3, 4)
gr.removeEdge(4, 4)

gr.display()

#    0 1 2 3 4
# 0| 0 0 0 1 0 
# 1| 0 0 1 0 1
# 2| 0 1 0 1 0
# 3| 1 0 1 0 0
# 4| 0 1 0 0 0