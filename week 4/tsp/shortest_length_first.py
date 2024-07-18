import math
from collections import namedtuple
from collections import defaultdict

Point = namedtuple("Points", ['x', 'y', 'ptno'])

def length(point1, point2):   
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
""" To check if adding a new edge makes the graph cyclic """
class graph:
    def __init__(self,V):
        self.V = V  # Number of vertices in the graph
        # List of lists to store the adjacency list of each vertex
        self.adj =  [ [] for _ in range(V)]
        # List to store the parent of each vertex in the disjoint set
        self.parent = list(range(V))
        # List to store the rank of each vertex in the disjoint set
        self.rank = [0] * V
    def addedge(self,u,v):
        # Find the root of the disjoint set containing vertex u
        parentU = self.find(u)
        # Find the root of the disjoint set containing vertex v
        parentV = self.find(v)
        if parentV == parentU: # If u and v are already in the same disjoint set, there is no need to add the edge
            return False 
         # If the rank of the disjoint set containing v is less than the rank of the disjoint set containing u
        if self.rank[parentU]>self.rank[parentV]:
            self.parent[parentV] =  parentU  # Make u the parent of v
        # If the rank of the disjoint set containing u is less than the rank of the disjoint set containing v
        elif self.rank[parentV]> self.rank[parentU]:
            self.parent[parentU] =  parentV  # Make v the parent of u
        else:  # If the rank of the disjoint set containing u is equal to the rank of the disjoint set containing v
            self.parent[parentU] = parentV
            self.rank[parentV]+=1
        self.adj[u].append(v)
        self.adj[v].append(u)
        return True
    def find(self,u):
        # If the parent of u is not u, i.e., u is not the root of its disjoint set
        if u < 0 or u >= len(self.parent):
           raise IndexError("Index out of range: {}".format(u))
        if self.parent[u]!=u:
            # Recursively find the root of the disjoint set containing u and update the parent of u to point directly to the root
           self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
""" Main greedy solution -
    Sort the edges in the increasing order of their length
    Keep selecting the next shortest edge if it does not form a loop in the graph 
    until number of edges equals number of vertices """
def sol(points,n):
    distance =  []
    for i in range(n-1):
        for j in range(i+1,n):
            distance.append([(length(points[i],points[j])),points[i],points[j]])
    # Create a list that stores the degree of each vertex
    degree = [0]*n
    # Sort the list in ascending order
    distance.sort()
    # Keep count of number of edges
    edge =0
    edge_list = []
    Graph1 =  graph(n)
    for i in distance:
        
        # If number of edges equals to number of points, no need to continue
        if edge == n:
            break
        
        # If both the vertices in the edgelist currently have degree less than two,
        # and adding edge to the grapg does not result in a loop, the edge is added 
        # to the graph and degrees of the vertices and number of edges are updated
        
        if degree[i[1].ptno] <2 and degree[i[2].ptno] <2:
            if Graph1.addedge(i[1].ptno , i[2].ptno)==True:
                edge_list.append([i[1].ptno,i[2].ptno])
                degree[i[1].ptno]+=1
                degree[i[2].ptno]+=1
                edge+=1
    
    # Find the vertices that have degree 1, there is a missing edge between these vertices 
    # which needs to be added       
    temp =  [0]*n
    for i in edge_list:
        temp[i[0]]+=1
        temp[i[1]]+=1

    edge_missing  = []            
    for i in range(n):
        if temp[i]==1:
            edge_missing.append(i)
            temp[i]+=1
    
    # Add the missing edge and return the edgelist
    edge_list.append(edge_missing)

    return edge_list
 # The greedy heuristic here prioritizes connecting all vertices with the least total edge weight, not necessarily visiting them in the most efficient order.

    
        
