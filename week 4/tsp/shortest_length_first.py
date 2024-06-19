import math
from collections import namedtuple
from collections import defaultdict

Point = namedtuple("Points", ['x', 'y', 'ptno'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

class graph:
    def __init__(self,V):
        self.V = V
        self.adj =  [ [] for _ in range(V)]
        self.parent = list(range(V))
        self.rank = [0] * V
    def addedge(self,u,v):
        parentU = self.find(u)
        parentV = self.find(v)
        if parentV == parentU:
            return False 
        if self.rank[parentU]>self.rank[parentV]:
            self.parent[parentV] =  parentU
        elif self.rank[parentV]> self.rank[parentU]:
            self.parent[parentU] =  parentV
        else:
            self.parent[parentU] = parentV
            self.rank[parentV]+=1
        self.adj[u].append(v)
        self.adj[v].append(u)
        return True
    def find(self,u):
        if u < 0 or u >= len(self.parent):
           raise IndexError("Index out of range: {}".format(u))
        if self.parent[u]!=u:
           self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

def sol(points,n):
    distance =  []
    for i in range(n-1):
        for j in range(i+1,n):
            distance.append([(length(points[i],points[j])),points[i],points[j]])
    
    degree = [0]*n
    edge_list = []
    distance.sort()
    edge =0
    Graph1 =  graph(n)
    for i in distance:
        if edge == n:
            break
        if degree[i[1].ptno] <2 and degree[i[2].ptno] <2:
            if Graph1.addedge(i[1].ptno , i[2].ptno)==True:
                edge_list.append([i[1].ptno,i[2].ptno])
                degree[i[1].ptno]+=1
                degree[i[2].ptno]+=1
                edge+=1
    temp =  [0]*n
    for i in edge_list:
        temp[i[0]]+=1
        temp[i[1]]+=1

    edge_missing  = []            
    for i in range(n):
        if temp[i]==1:
            edge_missing.append(i)
            temp[i]+=1
    edge_list.append(edge_missing)

    return edge_list

    
        
