import math 
import random
# random.seed(30)

def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)

""" a two opt function that optimizes the provided vehicle tours 
    by swapping two customers generated randomly in a particular tour
    and accepts the solution if the tour cost of generated tour is 
    less than original cost """
def opt_func (vehicletours, customers):
    depot =  customers[0]
    for vechicle_tour in vehicletours:
        tour_length =  len(vechicle_tour)
        if tour_length>=2: 
            cost_tour =0
            cost_tour+=length(depot, customers[vechicle_tour[0]])
            for i in range(tour_length-1):
                cost_tour+=length(customers[vechicle_tour[i]],customers[vechicle_tour[i+1]])
            cost_tour+=length(customers[vechicle_tour[-1]],depot)
            
            for _ in range(10000):   
                n1 =  random.randint(0,tour_length-1)
                n2 = random.randint(0,tour_length-1)
                vechicle_tour[n1],vechicle_tour[n2] = vechicle_tour[n2],vechicle_tour[n1]
                New_cost_tour =0
                New_cost_tour+=length(depot, customers[vechicle_tour[0]])
                for i in range(tour_length-1):
                    New_cost_tour+=length(customers[vechicle_tour[i]],customers[vechicle_tour[i+1]])
                New_cost_tour+=length(customers[vechicle_tour[-1]],depot)
                if New_cost_tour >= cost_tour:
                    vechicle_tour[n1],vechicle_tour[n2] = vechicle_tour[n2],vechicle_tour[n1]

    return vehicletours
            
            
        
    