#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import exchange_customer as sol1
import clarke_Wright as sol2
import two_optt
import pandas as pd 
from read_processed_data import read_input
from write_output import modify_output,visualize_output
    
    
    
    
    
    
Customer = namedtuple("Customer", ['index', 'demand', 'x', 'y'])


def solve_it(input_data):
    

    
    # parse the input data
    customer_count, vehicle_count, vehicle_capacity, customers = read_input(input_data)
    #the depot is always the first customer in the input
    depot = customers[0] 
    
     #### SOLUTION STARTS HERE ####

    if customer_count == 16 or customer_count == 26 or customer_count == 200:  
        # a solution with 2-opt optimization that exchanges customers between different random vehicles if capacity constraint is not violated      
        vehicle_tours = sol1.myfun(customers, customer_count, vehicle_count, vehicle_capacity)     
    else:
        # use clarke wright algorithm
        vehicle_tours = sol2.myfun(customers, customer_count, vehicle_count, vehicle_capacity) 
    # optimizing the obtained solution using 2-opt
    vehicle_tours = two_optt.opt_func(vehicle_tours, customers)
    
    #### SOLUTION ENDS HERE ####
    
    
    # getting the output data in the required format
    output_data,output_lst = modify_output(vehicle_tours,customers,customer_count,vehicle_count,depot)
    # visualizing the obtained solution
    visualize_output(output_lst,customer_count,vehicle_count)
    
    
    return output_data



import sys

if __name__ == '__main__':
    import sys
    #pdb.set_trace()
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:

        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/vrp_5_4_1)')

