# Graph dengan Adjacency List versi directed dan weighted

class Graph:
    def __init__(self):
        self.adjList = {}
    
    def addVertex(self, v):
        if v not in self.adjList: self.adjList[v] = {}          # kalau unweight pakai set, kalau weight pakai dict
    
    def addEdge(self, src, dest, weight):
        if src not in self.adjList: self.addVertex(src)
        if dest not in self.adjList: self.addVertex(dest)
        
        self.adjList[src][dest] = weight        # nested object [ src1: [dest1: weight, dest2: weight, ...], src2: ...]
        
    def removeEdge(self, src, dest):
        if src in self.adjList and dest in self.adjList[src]:
            del self.adjList[src][dest]
        else: print(f"Error: Edge {src}->{dest} tidak ditemukan")
    
    def removeVertex(self, v):
        if v in self.adjList:
            # Hapus incoming edges ke vertex ini
            for vertex in self.adjList:
                if v in self.adjList[vertex]: del self.adjList[vertex][v]
                
            # Hapus vertex
            del self.adjList[v]
        else: print(f"Error: {v} tidak ditemukan")
    
    def display(self):
        for vertex in sorted(self.adjList.keys()):
            neighbors = self.adjList[vertex]
            print(f"[{vertex}]: {neighbors}")
            

# Implementasi
gr = Graph()

gr.addVertex(0) 
gr.addVertex(3)
gr.addVertex(5)

gr.addEdge(0, 1, 9)
gr.addEdge(0, 3, 2)
gr.addEdge(0, 4, 3)
gr.addEdge(1, 2, 7)    
gr.addEdge(2, 3, 1)
gr.addEdge(3, 1, 5)
gr.addEdge(3, 4, 3)
gr.addEdge(3, 9, 5)
gr.addEdge(4, 5, 2)

gr.removeEdge(0, 2)
gr.removeVertex(7)

gr.addEdge(5, 6, 7)
gr.addEdge(6, 7, 2)

gr.display()