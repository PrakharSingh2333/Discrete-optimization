import math
import random
# random.seed(30)
from collections import namedtuple

def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)

""" function to return the total cost of the tour """
def total_cost(vehicle_tours, customers, vehicle_count):
    
    depot = customers[0]
    obj = 0

    for v in range(vehicle_count):
        vehicle_tour = vehicle_tours[v]
        
        if len(vehicle_tour) > 0:
            obj += length(depot,customers[vehicle_tour[0]])
            for i in range(0, len(vehicle_tour)-1):
                obj += length(customers[vehicle_tour[i]],customers[vehicle_tour[i+1]])
            obj += length(customers[vehicle_tour[-1]],depot)

    return obj

def demand(customers,v):
    curr_demand =0
    for i in v:
        curr_demand+= customers[i].demand
    return curr_demand
def opt_func (vehicletours, customers):
    depot =  customers[0]
    for vehicle_tours in vehicletours:
        tour_length =  len(vehicle_tours)
        if tour_length>=2: 
            cost_tour =0
            cost_tour+=length(depot, customers[vehicle_tours[0]])
            for i in range(tour_length-1):
                cost_tour+=length(customers[vehicle_tours[i]],customers[vehicle_tours[i+1]])
            cost_tour+=length(customers[vehicle_tours[-1]],depot)
            
            for _ in range(1000):   
                n1 =  random.randint(0,tour_length-1)
                n2 = random.randint(0,tour_length-1)
                vehicle_tours[n1],vehicle_tours[n2] = vehicle_tours[n2],vehicle_tours[n1]
                New_cost_tour =0
                New_cost_tour+=length(depot, customers[vehicle_tours[0]])
                for i in range(tour_length-1):
                    New_cost_tour+=length(customers[vehicle_tours[i]],customers[vehicle_tours[i+1]])
                New_cost_tour+=length(customers[vehicle_tours[-1]],depot)
                if New_cost_tour >= cost_tour:
                    vehicle_tours[n1],vehicle_tours[n2] = vehicle_tours[n2],vehicle_tours[n1]

    return vehicletours
def myfun(customers,customer_count,vehicle_count,vehicle_capacity):
    vehicle_tours = []
    
    remaining_customers = set(customers)
    remaining_customers.remove(customers[0])
    
    for v in range(0, vehicle_count):
        # print "Start Vehicle: ",v
        vehicle_tours.append([])
        capacity_remaining = vehicle_capacity
        while sum([capacity_remaining >= customer.demand for customer in remaining_customers]) > 0:
            used = set()
            order = sorted(remaining_customers, key=lambda customer: -customer.demand*customer_count + customer.index)
            for customer in order:
                if capacity_remaining >= customer.demand:
                    capacity_remaining -= customer.demand
                    vehicle_tours[v].append(customer.index)
                    # print '   add', ci, capacity_remaining
                    used.add(customer)
            remaining_customers -= used

    # checks that the number of customers served is correct
    assert sum([len(v) for v in vehicle_tours]) == len(customers) - 1
    print(vehicle_tours)
        
    for _  in range(100):
        vehicle_tours = opt_func(vehicle_tours,customers)
        v1 =  random.randint(0,vehicle_count-1)
        if len(vehicle_tours[v1])>=1:
            c1  =  random.randint(0,len(vehicle_tours[v1])-1)
            curr_cost = total_cost(vehicle_tours,customers,vehicle_count)
            for __ in range(100-_):
                v2 = random.randint(0,vehicle_count-1)
                if len(vehicle_tours[v2])>=1:
                    c2 =  random.randint(0,len(vehicle_tours[v2])-1)
                    if v2!=v1:
                        if demand(customers,vehicle_tours[v2])+customers[vehicle_tours[v1][c1]].demand-customers[vehicle_tours[v2][c2]].demand <= vehicle_capacity:
                            if demand(customers,vehicle_tours[v1])+customers[vehicle_tours[v2][c2]].demand - customers[vehicle_tours[v1][c1]].demand <= vehicle_capacity:
                                tour1 = vehicle_tours[v1]
                                tour2 = vehicle_tours[v2]
                                vehicle_tours[v1][c1],vehicle_tours[v2][c2] =   vehicle_tours[v2][c2],vehicle_tours[v1][c1]
                                vehicle_tours = opt_func(vehicle_tours, customers)
                                new_cost = total_cost(vehicle_tours,customers,vehicle_count)
                                if new_cost<curr_cost and demand(customers,vehicle_tours[v1]) <= vehicle_capacity and demand(customers,vehicle_tours[v2]) <= vehicle_capacity:
                                    curr_cost = new_cost
                                    break
                                else:
                                    vehicle_tours[v1] = tour1
                                    vehicle_tours[v2] = tour2
        
    return vehicle_tours
            
            
            
            
                   