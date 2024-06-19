from queue import PriorityQueue
from collections import defaultdict

def assign_colors(node_count, edge_count, edge_list):
    # Initialize data structures
    pq = PriorityQueue()  # Priority queue to store nodes based on degrees
    degrees = [0] * node_count  # Degrees of each node
    adjacency_list = defaultdict(list)  # Adjacency list to store neighbors of each node
    colors = [-1] * node_count  # Assigned colors for each node

    # Populate degrees and adjacency list based on the given edges
    for edge in edge_list:
        u, v = edge
        degrees[u] += 1
        degrees[v] += 1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Populate the priority queue with nodes sorted by degrees (in reverse order)
    for i in range(node_count):
        pq.put((-degrees[i], i))  # Negative degree for reverse ordering

    # Iteratively assign colors to nodes
    while not pq.empty():
        current_node = pq.get()[1]  # Get the node with the highest degree
        adjacent_colors = set()

        # Check colors of adjacent nodes
        for neighbor in adjacency_list[current_node]:
            if colors[neighbor] != -1:
                adjacent_colors.add(colors[neighbor])

        # Assign the lowest available color to the current node
        color = 0
        while color in adjacent_colors:
            color += 1

        colors[current_node] = color

    # Write the color assignment to the output file
    output_file = open("Output.txt", "w")
    max_color = 0
    output_file.write("Color Assignment Chart\n")
    for i in range(node_count):
        output_file.write(f"\nNode_{i}'s color -- {colors[i]}")
        max_color = max(max_color, colors[i])

    output_file.write("\n\nTotal colors used: " + str(max_color + 1))
    output_file.close()
    print("Output saved in Output.txt file")

    return [colors, max_color + 1]

