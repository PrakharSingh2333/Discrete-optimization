
import math
# find distance between two points
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
""" Working of greedy algorithm for TSP -
    Starting from point 0, select the nearest point to it and add an edge 
    from the set of remaining points(which are not yet connected), 
    continue this till all points are connected """
def greedy_sol(pts, n):
   
  res= [0]
  all_points =  [ pt for pt in range (1,n)]
  
  while len(res)<n:
     
     # Find the nearest point (from set of points not connected) to the last point in the current tour 
     # and add it to current tour and update set of remaining points
     
     least_distance  =  float('inf')
     nearest_point = -1
     for node in all_points:
        curr_dist = length(pts[res[-1]],pts[node])
        if curr_dist<least_distance:
           least_distance =  curr_dist
           nearest_point =  node
     res.append(nearest_point)
     all_points.remove(nearest_point)

  return res

  
