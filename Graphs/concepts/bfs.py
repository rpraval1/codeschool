"""
:Author: Pravallika
:Description: Breadth First Traversal or BFS for a Graph
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


    def BFS(self, s):
        visited = [False]*self.V

        queue = []

        queue.insert(0,s)
        visited[s] = True

        while queue:
            s = queue.pop()
            print(s, end=" ")

            for i in self.adjListArr[s]:
                if visited[i] == False:
                    queue.insert(0,i)
                    visited[i] = True

print("Directed: ")
newGraph = Graph(3,0)
newGraph.createGraph()
newGraph.addEdge(0,0)
newGraph.addEdge(0,1)
newGraph.addEdge(0,2)
newGraph.addEdge(2,1)
newGraph.addEdge(2,0)
newGraph.printGraph()

print("BFS: ")
newGraph.BFS(2)
