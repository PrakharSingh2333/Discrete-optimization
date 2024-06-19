import math
import random
def length(point1,point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

# def cal_distance(points,edge_list):
#     distance  =0
#     for i in edge_list:
#         cityAIndex = i[0]
#         cityBIndex = i[1]
#         cityA = points[cityAIndex]
#         cityB = points[cityBIndex]
#         distance  =  distance + length(cityA,cityB)
#     return distance 
# def two_opt(edge_list,i,j):
#     new_route =  edge_list.copy()
#     new_route[slice(i+1, j+1)] = new_route[slice(i+1, j+1)][::-1]
#     return new_route
def create_edge(edge_list,n):
    dict1 = {}
    dict2 = {}
    for i in edge_list:
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
    route  =  edge_list
    m =  100000
    for i in range(m):
        cityA =  random.randrange(0,n)
        cityB =  random.randrange(0,n)
        p1,p2,p3,p4 = edge_list[cityA][0],edge_list[cityA][1],edge_list[cityB][0],edge_list[cityB][1]
        if p1!=p3 and p1!=p4 and p2!=p3 and p2!=p4:
            cur_cost =  length(point[p1],point[p2])+length(point[p3],point[p4])
            new_cost1 =  length(point[p1],point[p3])+length(point[p2],point[p4])
            new_cost2 =  length(point[p1],point[p4])+length(point[p2],point[p3])
            if cur_cost > new_cost1 and cur_cost > new_cost2:
                flag1  =  False
                flag2  =  False
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

