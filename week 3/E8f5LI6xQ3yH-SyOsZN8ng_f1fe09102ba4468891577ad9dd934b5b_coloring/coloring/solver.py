#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
        Check if it is valid to color a given node with a specific color in a map.

        Args:
            colors (List[int]): The list of colors assigned to each node in the map.
            adj_list (List[List[int]]): The adjacency list representing the map.
            node (int): The current node being colored.
            node_count (int): The total number of nodes in the map.
            color (int): The color being considered for the current node.

        Returns:
            bool: True if it is valid to color the node with the given color, False otherwise.
        """
def color_graph(adj_list):
    num_vertices = len(adj_list)
    vertex_colors = [-1] * num_vertices
    available_colors = set(range(num_vertices))

    for vertex in range(num_vertices):
        if vertex_colors[vertex] != -1:
            continue

        neighbors = adj_list[vertex]
        available_neighbor_colors = available_colors - set(vertex_colors[neighbor] for neighbor in neighbors)
        if not available_neighbor_colors:
            return None

        vertex_colors[vertex] = min(available_neighbor_colors)
        available_colors.remove(vertex_colors[vertex])

        for neighbor in neighbors:
            if vertex_colors[neighbor] == -1:
                available_colors.add(vertex_colors[vertex])

    return len(vertex_colors), vertex_colors

def color_valid(colors, adj_list, node, node_count, color):
    for adjacent_node in adj_list[node]:
        if color[adjacent_node] == colors:
            return False
    return True
            
"""
            Recursively color a map with at most `max_color` colors.

            Args:
                node (int): The current node being colored.
                color (List[int]): The current coloring of the map.
                max_color (int): The maximum number of colors allowed.
                node_count (int): The total number of nodes in the map.
                adj_list (List[List[int]]): The adjacency list representing the map.

            Returns:
                bool: True if the map is successfully colored, False otherwise.
            """
def map_coloring(node,color,max_color,node_count,adj_list):
    if(node == node_count):
        return True
    for colors in range (1,max_color+1):
        if color_valid(colors,adj_list,node,node_count,color):
            color[node] = colors
            if map_coloring(node+1,color,max_color,node_count,adj_list):
                return True
            color[node]  =-1
    return False         

# function which give the maximum color and colors of the map with which it is filled 
def find_minimum_color(node_count,adj_list):
    for max_color in range(1,node_count+1):
        color =  [-1 for _ in range(node_count)]
        if map_coloring(0,color,max_color,node_count,adj_list):
            return max_color,color




def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    # making adjacent list to traverse while filling map
    adj_list  =  [[] for _ in range(node_count)]
    for u,v in edges :
        adj_list[u].append(v)
        adj_list[v].append(u)
    min_color,result=  color_graph(adj_list)



    


    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(min_color) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, result))

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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')


