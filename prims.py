
import math

class Vertex:
    def __init__(self, val):
        self.val = val
        self.connected = False
        self.visited = False
        #self.cost = math.inf
        
        

class Graph():

    def __init__(self, adjacency_matrix):
        """ 
        Graph initialized with a weighted adjacency matrix 
        
        Attributes
        ----------
        adjacency_matrix : 2D array
            non-negative integers where adjacency_matrix[i][j] is the weight of the edge i to j,
            with 0 representing no edge

        """

        self.adjacency_matrix = adjacency_matrix
        
        # Add more class variables below as needed, such as n:
        #self.N = len(adjacency_matrix)
        self.vertices = []
        

    
    def Prim(self):
        """
        Use Prim-Jarnik's algorithm to find the length of the minimum spanning tree starting from node 0

        Returns
        -------
        int
            Weighted length of tree

        """
        
        n = len(self.adjacency_matrix)
        
        if n == 0:
            return 0
        #print("n is: ", n)
        sum = 0
        for i in range(n):
            self.vertices.append(Vertex(i))
            
        rows, cols = (n, n) 
        options = [[False for i in range(cols)] for j in range(rows)]
        
        self.vertices[0].connected = True
        self.vertices[0].visited = True
        connected = []
        currV = 0
        
        #exploring edges connected to currV
        
        connected.append(0)
        
        while len(connected) < n:
            
            minEdge = math.inf
            
            #vthRow = self.adjacency_matrix[currV]
#             print("options before:")
#             for row in options:
#                 print(row)
            for i in range(n):#I thought I was only traversing one row but...
                #print("i is: ",i)
                if (self.adjacency_matrix[currV][i] != 0) and (self.vertices[i].visited == False):
                    #print("adding to options:",currV, ",",i, "-", self.adjacency_matrix[currV][i])
                    #print("options[currV] before:", options[currV][i])
                    
                    options[currV][i] = True
                    #print("options after setting just one cell to True:")
                    #for row in options:
                        #print(row)
                    
                    
        #going through whole options matrix to find min edge
            self.vertices[currV].visited = True
            
            for i in range(n):
                for j in range(n):
                    
                    if (self.adjacency_matrix[i][j] < minEdge) and (options[i][j] == True) and (self.vertices[j].connected == False): #elligible edge with no loops
                        minEdge = self.adjacency_matrix[i][j]
                        #print("minEdge:", minEdge, "options:", options[i][j])
                        startV = i
                        endV = j

            sum = sum + minEdge
            self.vertices[endV].connected = True
            currV = self.vertices[endV].val
            #print("currV:",currV)
            connected.append(endV)
            options[startV][endV] = False
            
        #print(sum)
        return sum


#  Example use case:

# G[r][c]
# G[0] => [0, 10, 11, 33, 60]
# topRow = G[0]
# for num in topRow:
#     do something with the num

# G = Graph([[0, 10, 11, 33, 60],
#             [10, 0, 22, 14, 57],
#             [11, 22, 0, 11, 17],
#             [33, 14, 11, 0, 9],
#             [60, 57, 17, 9, 0]])

# A = Graph([[0, 10] ,
#             [10, 0]])

# #A = Graph([[0, 1, 9] ,
#             [1, 0, 7],
#             [9, 7, 0]])
#G.Prim()
# assert G.Prim() == 41
#assert A.Prim() == 10
#assert A.Prim() == 8