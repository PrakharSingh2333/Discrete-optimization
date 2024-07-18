import math
from collections import namedtuple


Customer = namedtuple("Customer", ['index', 'demand', 'x', 'y'])
# to calculate the distance between two customers
def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)
# function to return input data in required format which contain customer count, vehicle count and vehicle capacity
def read_input(input_data):
    lines = input_data.split('\n')

    parts = lines[0].split()
    customer_count = int(parts[0])
    vehicle_count = int(parts[1])
    vehicle_capacity = int(parts[2])
    
    customers = []
    for i in range(1, customer_count+1):
        line = lines[i]
        parts = line.split()
        customers.append(Customer(i-1, int(parts[0]), float(parts[1]), float(parts[2])))
    
    return customer_count, vehicle_count, vehicle_capacity, customers
        