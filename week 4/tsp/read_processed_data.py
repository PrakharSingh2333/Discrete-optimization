import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y', 'ptno'])
# to determine the distance between two points
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)



def read_input():
    file_location =r"C:\Users\olw08\OneDrive - ORMAE\Discrete optimization\week 4\tsp\data\tsp_76_2"
    with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = [] 
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1]),i-1))
    return points,nodeCount

    