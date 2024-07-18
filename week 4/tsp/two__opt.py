import math
import random

def length(point1,point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

""" Function to create output in the desired format, i.e.,
     a list on vertices in the order they are visited from
     a list of edges """
def create_edge(edge_list,n):
    
    # Using two dictionaries to store where each vertex is connected
    dict1 = {}
    dict2 = {}
    for i in edge_list:
        
        # since a vertex is connected to two other vertices,
        # each dictionary will store one vertex 
        if i[0] in dict1:
            dict2[i[0]] = i[1]
        else:
            dict1[i[0]] = i[1]

        if i[1] in dict1:
            dict2[i[1]] = i[0]
        else:
            dict1[i[1]] = i[0]
        
    res = [0]
    while len(res) < n:

        if dict1[res[len(res)-1]] in res:
            res.append(dict2[res[len(res)-1]])
        else:
            res.append(dict1[res[len(res)-1]]) 

    return res
            


def multiple_loops1(edge_list,cityA,cityB,a,b,c,d,n):
    edgelistcopy = edge_list
    edgelistcopy[cityA] = [a,b]
    edgelistcopy[cityB] = [c,d]
    tempelate  =  create_edge(edgelistcopy,n)
    template2 =  set(tempelate)
    if len(template2) < n:
       edgelistcopy[cityA] = [a,c]
       edgelistcopy[cityB] = [b,d] 
       return 1
    return 0
def multiple_loops2(edges, e1, e2, a, b, c, d, n):
    edgelistcopy = edges
    edgelistcopy[e1] = [a,b]
    edgelistcopy[e2] = [c,d]
    tempset2 = create_edge(edgelistcopy, n)
    tempset = set(tempset2)
    # print(len(tempset))
    if len(tempset) < n:
        edgelistcopy[e1] = [a,c]
        edgelistcopy[e2] = [d,b]
        return 1
    return 0
def improve(point,n,edge_list):
    
    # Using already available feasible solution  
    route  =  edge_list
    m =  100000
    
    # Select two edges at random and try to change configuration if of less cost
    for i in range(m):
        cityA =  random.randrange(0,n)
        cityB =  random.randrange(0,n)
        p1,p2,p3,p4 = edge_list[cityA][0],edge_list[cityA][1],edge_list[cityB][0],edge_list[cityB][1]
        # To check weather these two edges are not connected or same
        if p1!=p3 and p1!=p4 and p2!=p3 and p2!=p4:
            
             # Compare the current cost of the solution with costs of other two configurations
            cur_cost =  length(point[p1],point[p2])+length(point[p3],point[p4])
            new_cost1 =  length(point[p1],point[p3])+length(point[p2],point[p4])
            new_cost2 =  length(point[p1],point[p4])+length(point[p2],point[p3])
            
             # For both new configurations, one of the configuration will form multiple loops in the tour
             
            if cur_cost > new_cost1 and cur_cost > new_cost2:
                flag1  =  False
                flag2  =  False
                
                # Select the tour that does not form multiple loops and has lowest tour cost
                
                if multiple_loops1(edge_list,cityA,cityB,p1,p3,p2,p4,n)==0:
                    flag1 =  True
                if multiple_loops2(edge_list,cityA,cityB,p1,p4,p2,p3,n)==0:
                    flag2 =  True
                if flag1==True and flag2==True:
                    if new_cost1>new_cost2:
                        route[cityA] = [p1,p4]
                        route[cityB] = [p2,p3]
                    else:
                        route[cityA] = [p1,p4]
                        route[cityB] = [p2,p3]
                elif flag1==True:
                    route[cityA] = [p1,p3]
                    route[cityB] = [p2,p4]
                elif flag2==True:
                    route[cityA] = [p1,p4]
                    route[cityB] = [p2,p3]
            elif new_cost1 < cur_cost:
                if multiple_loops1(edge_list,cityA,cityB,p1,p3,p2,p4,n)==0:
                    route[cityA] = [p1,p3]
                    route[cityB] = [p2,p4]
            elif new_cost2 < cur_cost:
                if multiple_loops2(edge_list,cityA,cityB,p1,p4,p2,p3,n)==0:
                    route[cityA] = [p1,p4]
                    route[cityB] = [p2,p3]
    
    return create_edge(route,n)

