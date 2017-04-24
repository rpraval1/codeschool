"""
:Author: Pravallika
:Description: Depth First Traversal or DFS for a Graph
"""

#Structure to represent a graph
#V = number of vertices
#adjListArr = array of List which will hold our dests
class Graph(object):
    def __init__(self, V, type):
        self.V = V
        self.type = type
        self.adjListArr = [None]*V

    def createGraph(self):
        for i in range(self.V):
            self.adjListArr[i] = []

    def addEdge(self, src, dest):
        if dest not in self.adjListArr[src]:
            self.adjListArr[src].append(dest)

        #if graph is undirected, dest to src also forms an edge
        if self.type:
            if src not in self.adjListArr[dest]:
                self.adjListArr[dest].append(src)

    def printGraph(self):
        for adjLists in self.adjListArr:
            print(adjLists)


    #DFS given starting point
    def DFS_I(self,s):
        visited = [False]*self.V

        self.DFSUtil(s,visited)

    def DFS(self):
        visited = [False]*self.V

        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i,visited)

    def DFSUtil(self,s,visited):
        visited[s] = True
        print(s, end=" ")

        for i in self.adjListArr[s]:
            if visited[i] == False:
                self.DFSUtil(i,visited)

print("UnDirected: ")
g = Graph(4,0)
g.createGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()

g = Graph(4,0)
g.createGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()

print("DFS: with starting: ")
g.DFS_I(2)
print()
print("DFS: ")
g.DFS()
