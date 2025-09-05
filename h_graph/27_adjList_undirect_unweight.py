# Graph dengan Adjacency List versi undirected dan unweighted

class Graph:
    def __init__(self):
        self.adjList = {}
    
    def addVertex(self, v):
        if v not in self.adjList: self.adjList[v] = set()
    
    def addEdge(self, v1, v2):
        if v1 not in self.adjList: self.addVertex(v1)
        if v2 not in self.adjList: self.addVertex(v2)
        
        self.adjList[v1].add(v2)
        self.adjList[v2].add(v1)
        
    def removeEdge(self, v1, v2):
        if v1 in self.adjList and v2 in self.adjList[v1]:
            self.adjList[v1].discard(v2)
            self.adjList[v2].discard(v1)
        else: print(f"Error: Edge {v1}-{v2} tidak ditemukan!")
    
    def removeVertex(self, v):
        if v in self.adjList:
            # Hapus vertex dari adjList vertices lain
            for neighbor in list(self.adjList[v]):
                self.adjList[neighbor].discard(v)
            
            # Hapus vertex
            del self.adjList[v]
        else: print(f"Error: Vertex {v} tidak ditemukan!")
    
    def display(self):
        for vertex in sorted(self.adjList.keys()):
            neighbors = sorted(list(self.adjList[vertex]))
            print(f"[{vertex}]: {neighbors}")


# Implementasi
gr = Graph()

gr.addVertex(0) 
gr.addVertex(3)
gr.addVertex(5)

gr.addEdge(0, 1)
gr.addEdge(0, 2)
gr.addEdge(0, 3)
gr.addEdge(0, 9)
gr.addEdge(1, 2)    
gr.addEdge(2, 3)
gr.addEdge(3, 4)
gr.addEdge(4, 5)

gr.removeEdge(2, 0)
gr.removeVertex(4)

gr.addVertex(99)    # adjList = dinamis, bisa menambah vertex atau edge tanpa batasan
gr.addEdge(5, 6)
gr.addEdge(6, 7)

gr.display()
