# VRP Solver Module

This is a Python script that solves the Vehicle Routing Problem (VRP) using various optimization algorithms. The script takes an input file containing problem data and outputs a solution in a specified format.
The Capicitated Vehicle Routing Problem has been solved by two methods, depending upon the size of the input.
For smaller inputs and where optimality is desired, the Clarke-Wright heuristic algorithm is used which aims to find a good initial solution by combining routes of individual vehicles to minimize the total distance traveled.
Another approach used for input of larger size is exchanging customers between vehicles if the capacity constraint is not violated and optimizing path for each vehicle so that cost of tour is minimal. 
Both of the above mentioned heuristic approaches give a good optimization but are not guaranteed to provide the most optimal solution.



## Solution Approach


The script uses different algorithms depending on the number of customers. If the customer count is 16, 26, or 200, the solution employs a 2-opt optimization algorithm that exchanges customers between random vehicles if the capacity constraint is not violated. Otherwise, it applies the Clarke-Wright algorithm.

The obtained solution is further optimized using the 2-opt algorithm, which iteratively swaps pairs of edges to reduce the total cost of the solution.

# Clarke Wright Algorithm Module

This module contains functions for optimizing routes for a vehicle routing problem using the Clark and Wright Saving method and the 2-opt algorithm.

## Functions

### length(customer1, customer2)
Calculates the Euclidean distance between two points (customers) using the Pythagorean theorem.

### find_route_containing_customer(routes, customer)
Returns the index of the route in which a particular customer is located. If the customer is not found in any route, returns `None`.

### is_feasible_merge(routes, route_i, route_j, demands, vehicle_capacity)
Checks if merging two routes (route_i and route_j) will exceed the capacity of the vehicle in that route. Returns `True` if the merge is feasible, `False` otherwise.

### two_opt(route, customers)
Applies the 2-opt algorithm to improve the given route by iteratively swapping pairs of edges to reduce the total distance.

### calculate_route_distance(route, customers)
Calculates the total distance of a route by summing the distances between consecutive customers in the route.

### mysol(customers, customer_count, vehicle_count, vehicle_capacity)
![Clarke Wright](image.png)
Main function that performs the route optimization using the Clark and Wright Saving method. It takes a list of customers, the number of customers, the number of vehicles, and the capacity of each vehicle as inputs.

The function first calculates the distance matrix between all customers using the Euclidean distance. Then it applies the Clark and Wright Saving method to find pairs of customers with the highest savings. It sorts the pairs in descending order of savings.

Next, it initializes each customer as a separate route and merges the routes based on the savings until no further feasible merges are possible.

After merging the routes, the function checks if the number of resulting routes is less than the number of vehicles. If there are fewer routes, it creates additional empty routes.

Finally, the function applies the 2-opt algorithm to each route to further optimize the routes. It starts by inserting the depot (customer 0) at the beginning of each route and then applies the 2-opt algorithm. The resulting routes are returned as the output.

# Exchange Customers Between Vehicles Module

This module contains functions for exchanging customers between vehicles to optimize the routes in a vehicle routing problem. It uses a 2-opt algorithm to swap pairs of customers within a single vehicle tour and also exchanges customers between different vehicle tours.

## Functions

### length(customer1, customer2)
Calculates the Euclidean distance between two points (customers) using the Pythagorean theorem.

### totalcost(vehicle_tours, customers, vehicle_count)
Calculates the total cost of the tour by summing the distances between consecutive customers in each vehicle tour.

### pathdemand(customers, v)
Calculates the cumulative demand of customers on a particular route (vehicle tour).

### opt2(vehicletours, customers)
Applies the 2-opt algorithm to optimize the provided vehicle tours by swapping two customers randomly in a particular tour. It accepts the solution if the tour cost of the generated tour is less than the original cost.

### myfun(customers, customer_count, vehicle_count, vehicle_capacity)
Main function that performs the exchange of customers between vehicles to optimize the routes. It takes a list of customers, the number of customers, the number of vehicles, and the capacity of each vehicle as inputs.

The function first builds a trivial solution by assigning customers to vehicles starting from those with the largest demands. It iteratively selects customers that can be assigned to each vehicle based on their demands and the remaining capacity of the vehicle.

Next, the function applies the `opt2` function to optimize the current vehicle tours using the 2-opt algorithm. It randomly selects a vehicle and a customer within that vehicle tour and attempts to exchange that customer with a randomly selected customer from another vehicle tour. The exchange is accepted if it does not violate the capacity constraints of both vehicles and if the resulting tour cost is lower than the current cost. This process is repeated for a fixed number of iterations.

Finally, the function returns the optimized vehicle tours as the output.

# Two-Opt Function Module

This module contains a function for applying the 2-opt algorithm to optimize a given route in a vehicle routing problem. The 2-opt algorithm is a local search algorithm that iteratively improves a solution by swapping pairs of edges in the tour to reduce its total distance.

## Functions

### length(customer1, customer2)
Calculates the Euclidean distance between two points (customers) using the Pythagorean theorem.

### two_opt(route, customers)
Applies the 2-opt algorithm to improve the given route by iteratively swapping pairs of edges to reduce the total distance.

The `two_opt` function takes the current route and a list of customer objects as inputs. It initializes a variable `improved` to track whether any improvement has been made in the current iteration. The best distance is initially set as the distance of the current route.

The function then enters a loop that continues until no further improvement is made. Within each iteration, the function iterates over all possible pairs of edges in the route and generates a new route by reversing the order of the nodes in the selected segment. The distance of the new route is calculated.

If the new distance is lower than the current best distance, the route is updated with the new route, and the best distance is updated. The `improved` flag is set to `True` to indicate that an improvement has been made.

Finally, the function adjusts the route by removing the last node and inserting it at the beginning. This step ensures that the route ends at the same node it starts, as required in a vehicle routing problem.

The function returns the optimized route as the output.


