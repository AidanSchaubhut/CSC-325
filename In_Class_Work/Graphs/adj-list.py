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
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self, n): # vertex in Graph
        return (n in self.vertList)
        # Since we are using the dict as backing, we can use the already implemented __contains__
        # function that was created from the dict class. 
    
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
    
    # This itterates over the values in the vertList
    def __iter__(self):
        return iter(self.vertList.values())

def main():
    graph = Graph()

    for i in range(6):
        graph.addVertex(i)
    
    graph.addEdge(0, 1, 5)


main()