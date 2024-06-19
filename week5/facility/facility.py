from ortools.linear_solver import pywraplp
import math 

# tell the distance between the facilities and the customer 
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
def main(facilities,customer):
    no_f =  len(facilities)
    no_c =  len(customer)
    solver = pywraplp.Solver.CreateSolver("SCIP")
    open = {}
    x    = {}
    time_limit = 1800
    if no_f >= 500:
        time_limit *= 3
    solver.SetTimeLimit(int(time_limit * 1000))
     # DECISION VARIABLES
    # The decision variables are - for each facility, a boolean variable that denotes the status of facility (open/closed)
    # and other (number of facilities * number of customers) variables that denote if facility f is serving customer c
    # for all f belonging to set of Facilities and c belonging to set of Customers
    for i in range(no_f):
        open[i] = solver.BoolVar(f"Facility {i}")

    for i in range(no_f):
        for j in range (no_c):
            x[i,j] = solver.BoolVar(f"does facility {i}  serve customer {j}")


    #CONSTRAINTS

    # Each customer should be served by exactly one facility
    for i in range (no_c):
        # tempsum=0
        # tempsum = solver.sum(x[j,i] for j in range(no_f))
        solver.Add(solver.Sum(x[j,i] for j in range(no_f)) == 1)

    # The sum of demands of customers served by a particular facility should be less than maximum capacity of the facility
    
    for i in range(no_f):
        # # sumofdemand =0
        # sumofdemand=solver.sum(customer[j].demand*x[i,j] for i in range(no_c))
        solver.Add(solver.Sum(customer[j].demand*x[i,j] for j in range(no_c))<=facilities[i].capacity)

    # Facility can only serve a customer if its open
    for i in range(no_f):
        # sumrow = 0
        # sumrow =solver.sum(x[i,j] for j in range(no_c))
        solver.Add(solver.Sum(x[i,j] for j in range(no_c))<=no_c*open[i])

    # OBJECTIVE
    # the objective is minizing the setup cost of facilities and minimizing the sum of distance between customers and facilities 

    sumsetup =0
    for i in range(no_f):
        sumsetup+=facilities[i].setup_cost*open[i]
    sumdist =0
    for i in range(no_f):
        for j in range(no_c):
            sumdist+=length(facilities[i].location,customer[j].location)*x[i,j]
    
    solver.Minimize(sumdist+sumsetup)
    solver.Solve()
    
    res =  [-1]*no_c
    for i in range(no_f):
        for j in range(no_c):
            if(x[i,j].solution_value()==1):
                res[j] = i
    return res            

            
