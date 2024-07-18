#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import greedy
import two__opt
import shortest_length_first as slf
import pdb
import pandas as pd
from read_processed_data import read_input
from write_output import modify_output,visualize_output
Point = namedtuple("Point", ['x', 'y', 'ptno'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def solve_it_2():
    #reading the input from the read input function
    points,nodeCount = read_input()
    solution = range(0, nodeCount)
    # forming the solution based on the nodecount 
    
    if nodeCount == 33810: # greedy solution for larger node count
     solution  = greedy.greedy_sol(points, nodeCount) 
    elif nodeCount == 574: # 2-opt solution
     edge_list = []
     for i in range(0,nodeCount-1):
        edge_list.append([i,i+1])
     edge_list.append([nodeCount-1,0])
     solution = two__opt.improve(points,nodeCount,edge_list)
    else:  # shortest length first initial feasible solution 
     edgelist = slf.sol(points,nodeCount) 
     solution  =  two__opt.improve(points,nodeCount,edgelist)
    # formulating the output in the desired format
    output_req_format = modify_output(solution,points,nodeCount)
    # visualizing the output and saving it in a excel file 
    visualize_output(solution)
    return output_req_format
    
    
    
    
    
    




import sys

if __name__ == '__main__':
    # import sys
    # if len(sys.argv) > 1:
    #     file_location = sys.argv[1].strip()
        # with open(file_location, 'r') as input_data_file:
        #     input_data = input_data_file.read()
        # print(solve_it(input_data))
    # else:
    #     print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')
    # file_location =r"C:\Users\olw08\OneDrive - ORMAE\Discrete optimization\week 4\tsp\data\tsp_76_2"
    # with open(file_location, 'r') as input_data_file:
    #         input_data = input_data_file.read()
    # print(solve_it(input_data))
    solve_it_2()

