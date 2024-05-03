from queue import Queue

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    class __Vertex:
        def __init__(self, key):
            self.id = key
            self.connectedTo = {} # Keys are the objects of the destinations, values is the weight of the edges
        
        def getId(self):
            return self.id
        
        def getConnections(self):
            return self.connectedTo.keys() # Returns the references to the objects of the vertex class
        
        def getWeight(self, nbr):
            return self.connectedTo[nbr]
        
        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self) -> str:
            return f"connected to: {str([x.id for x in self.connectedTo])}"

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    # We input the label for the vertex but we are returning the actual vertex object
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def addEdge(self, source, destination, weight = 0):
        # If the source is not in the Graph yet, add it to the graph
        if source not in self.vertList:
            # We are adding this to a variable bc addVertex will return the newly created Vertex at the end of the function
            newVertex = self.addVertex(source)
        # Same with the destination
        if destination not in self.vertList:
            newVertex = self.addVertex(destination)

        # This is the function that will add the edge connecting the source to the destination
        self.vertList[source].addNeighbor(self.vertList[destination], weight)

    def getVertices(self):
        return self.vertList.keys()
    
    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end=" ")
            visited.add(s)
            for nextNdoe in [x.id for x in self.vertList[s].connectedTo]:
                self.dfs(nextNdoe, visited)
    
    # The implementation for the stack in this case was found at https://www.geeksforgeeks.org/stack-in-python/
    def dfs_iter(self, s, visted=None):
        if visted is None:
            visted = set()

        stack = []
        stack.append(s)
        while len(stack) != 0:
            current_node = stack.pop()
            visted.add(current_node)
            print(current_node, end=' ')

            for next_node in [x.id for x in self.vertList[current_node].connectedTo]:
                if next_node not in visted:
                    stack.append(next_node)
                visted.add(next_node)


    def bfs(self, s, visited=None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end=' ')

            for next_node in [x.id for x in self.vertList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)


    def __contains__(self, n): # vertex in Graph
        return (n in self.vertList)
        # Since we are using the dict as backing, we can use the already implemented __contains__
        # function that was created from the dict class. 
    
    # This itterates over the values in the vertList
    def __iter__(self):
        return iter(self.vertList.values())

def main():

    graph = Graph()

    for i in range(6):
        graph.addVertex(i)

    graph.addEdge(0,1)
    graph.addEdge(1,0)

    graph.addEdge(0,2)
    graph.addEdge(2,0)

    graph.addEdge(0,3)
    graph.addEdge(3,0)

    graph.addEdge(0,4)
    graph.addEdge(4,0)

    graph.addEdge(1,2)
    graph.addEdge(2,1)

    graph.addEdge(2,3)
    graph.addEdge(3,2)

    graph.addEdge(2,5)
    graph.addEdge(5,2)

    graph.addEdge(3,4)
    graph.addEdge(4,3)

    graph.addEdge(4,5)
    graph.addEdge(5,4)

    graph.addEdge(3,5)
    graph.addEdge(5,3)

    print()
    for k, v in graph.vertList.items():
        print(k, v)

    print()

    graph.dfs_iter(3)

main()