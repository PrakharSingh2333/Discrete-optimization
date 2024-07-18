import math 
import random
import numpy as np

def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)

""" Returns the route in which particular customer is located """
 
def find_route_containing_customer(vehicle_tours, customer):
    for i,vechicle in enumerate(vehicle_tours):
        if customer in vechicle:
            return i

    return None

"""checks weather merging the customer in route does not exceed the capacity of vehicle in that route """

def is_feasible_merge(vehicle_tours, route_i, route_j, demands, vehicle_capacity):
    
    total_demand =  sum(demands[customer] for customer in vehicle_tours[route_i])+ sum(demands[customer] for customer in vehicle_tours[route_j])

    return total_demand <= vehicle_capacity

"""Calculates the total distance of a route"""
  
def calculate_route_distance(route, customers):
  
    total_distance = 0

    for i in range(len(route)):
        total_distance += length(customers[route[i]], customers[route[(i + 1) % len(route)]])

    return total_distance

""" Applies the 2-opt algorithm to improve the given route"""
 
def two_opt(route, customers):
   
    improved = True
    best_distance = calculate_route_distance(route, customers)
    
    while improved:
        improved = False
        for i in range(0, len(route) - 1):
            for j in range(i + 2, len(route)):
                new_route = route.copy()
                new_route[i:j+1] = reversed(route[i:j+1])  # Reverse the order of the nodes in the selected segment
                new_distance = calculate_route_distance(new_route, customers)
                
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
                    improved = True
        route.insert(0, route[len(route)-1])
        route.pop()
    return route
       

def myfun(customers,customer_count,vehicle_count,vehicle_capacity):
    # distance matrix for all pairs of customers
    D = []
    depot = customers[0]
    for i in range(customer_count):
        temp = []
        for j in range(customer_count):
            temp.append(length(customers[i], customers[j]))
        D.append(temp)
    demand = [customer.demand for customer in customers]
    savings = np.zeros((customer_count, customer_count))
    # saving matrix shows the savings between two customers when they are added to the same route
    for i in range(customer_count):
        for j in range(i+1,customer_count):
            savings[i][j] = D[depot.index][i]+D[depot.index][j]-D[i][j]
            savings[j][i] = savings[i][j]
    vehicle_tours = [[i] for i in range (1,customer_count)]
    saving_indices = np.argsort(-savings, axis=None)
    saving_i,saving_j = np.unravel_index(saving_indices,savings.shape)
    s_i= []
    s_j = []
    k=0
    while k < len(saving_i):
        if saving_i[k]!=0 and saving_j[k]!=0 and saving_i[k]!=saving_j[k]:
            s_i.append(saving_i[k])
            s_j.append(saving_j[k])
        k+=1
    # to check weather merging two customers in route does not exceed the capacity of vehicle
    for k in range(len(s_i)):
        i,j = s_i[k],s_j[k]
        route_i = find_route_containing_customer(vehicle_tours,i)
        route_j = find_route_containing_customer(vehicle_tours,j)
        if route_i!=route_j and is_feasible_merge(vehicle_tours,route_i,route_j,demand,vehicle_capacity):
            vehicle_tours[route_i]+=vehicle_tours[route_j]
            del vehicle_tours[route_j]
    cnt  =0    
    # if the vehicle count is greater than the length(vehicle_tour) then append the remaining vehicles in vehicle_tour   
    if len(vehicle_tours) < vehicle_count:
        cnt  =  vehicle_count - len(vehicle_tours)
    for v in range(cnt):
        vehicle_tours.append([])
    
    for v in range(vehicle_count):
        if len(vehicle_tours[v]) > 1:
            vehicle_tours[v].insert(0, depot.index)
            vehicle_tours[v] = two_opt(vehicle_tours[v], customers)
            if vehicle_tours[v] is not None:
                temp = vehicle_tours[v].copy()
            else:
             temp = []
            #temp = vehicle_tours[v].copy()
            vehicle_tours[v] = []
            for i in temp:
                if i != 0:
                    vehicle_tours[v].append(i)
                else:
                    break
            for i in reversed(temp):
                if i != 0:
                    vehicle_tours[v] = [i] + vehicle_tours[v]
                else:
                    break

    return vehicle_tours
        
            