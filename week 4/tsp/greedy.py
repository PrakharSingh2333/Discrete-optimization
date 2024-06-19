
import math
# find distance between two points
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def greedy_sol(pts, n):
  res= [0]
  all_points =  [ i for i in range (1,n)]
  while len(res)<n:
     least_distance  =  float('inf')
     nearest_point = -1
     for i in all_points:
        curr_dist = length(pts[res[-1]],pts[i])
        if curr_dist<least_distance:
           least_distance =  curr_dist
           nearest_point =  i
     res.append(nearest_point)
     all_points.remove(nearest_point)

  return res

  