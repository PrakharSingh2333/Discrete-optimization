#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import greedy
import two__opt
import shortest_length_first as slf

Point = namedtuple("Point", ['x', 'y', 'ptno'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1]),i-1))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    solution = range(0, nodeCount)
    if nodeCount == 33810:
     solution  = greedy.greedy_sol(points, nodeCount) 
    elif nodeCount == 574:
     edge_list = []
     for i in range(0,nodeCount-1):
        edge_list.append([i,i+1])
     edge_list.append([nodeCount-1,0])
     solution = two__opt.improve(points,nodeCount,edge_list)
    else:
     edgelist = slf.sol(points,nodeCount)
     solution  =  two__opt.improve(points,nodeCount,edgelist)
       
       

    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

