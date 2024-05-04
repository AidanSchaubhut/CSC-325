import sys
from queue import Queue

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"  

        def __repr__(self):
            return str(self.id )

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
                self.dfs(next_node, visited)        

    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):

        # Function is used to find the reference of the cluster that a vertex is contained in
        def findVertex(vertex) -> set:
            for cluster in vertices_sets:
                if vertex in cluster:
                    return cluster
            return None
        
        vertices_sets = set()
        edges_dict = dict()
        MST = set()
        
        ### WRITE YOUR CODE HERE ###

        # Fill vertices_sets with all verticies from the graph
        for vert in self.getVertices():
            newVert = frozenset([vert]) # The frozen set idea came from https://www.geeksforgeeks.org/how-to-create-a-set-of-sets-in-python/#
            vertices_sets.add(newVert)

        # Init the dictionary with all the edges
        for source in self.getVertices():
            for dest in self.getVertex(source).getConnections():
                edge = tuple(sorted((source, dest.getId())))  # Sort the vertices in the edge tuple
                edges_dict[edge] = self.getVertex(source).getWeight(dest)

        # Sort the dictionary by the weights
        # This method for sorting the dictionary came from https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sorted_edges = sorted(edges_dict.items(), key=lambda x:x[1])
        edges_dict = dict(sorted_edges)

        for (source, destination) in edges_dict:
            
            set1 = findVertex(source)
            set2 = findVertex(destination)
            
            if set1 != set2:
                # Adding the edge and weight to the MST
                tba = ((source, destination), edges_dict[(source, destination)])
                MST.add(tba)
                # Creates a new cluster containing the other two clusters
                newSet = set1.union(set2)
                # Removes the old clusters and added the combined one to vertices_sets
                vertices_sets.remove(set1)
                vertices_sets.remove(set2)
                vertices_sets.add(newSet)

        return MST

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()
    ### WRITE YOUR CODE HERE ###
    print("Graph adjacency list:")
    for k, v in graph.verList.items():
        print(k, v)
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 