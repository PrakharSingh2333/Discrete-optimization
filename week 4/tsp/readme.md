# Traveling Salesman Problem Implementation

This repository contains an implementation of the Traveling Salesman Problem (TSP) using various approaches.

## Problem Description

The Traveling Salesman Problem is a classic optimization problem where the goal is to find the shortest possible route that visits a set of cities and returns to the starting city. It is an NP-hard problem with many real-world applications.

## Approaches

### Greedy Solution

One of the approaches implemented is the greedy solution, which works as follows:
- Starting from a random point (e.g., point 0), find its nearest point and add an edge.
- Continue adding edges from the last point in the tour by finding the nearest point that does not create a loop.
- When all possible edges are exhausted, find the points in the tour that have a degree of 1 and add the missing edge between these points.



### 2-opt Technique for Optimization

One of the techniques used for optimizing a feasible solution is the 2-opt technique. It works as follows:
- Remove two edges from the tour.
- Find a configuration with two new edges that has the minimum cost over a number of iterations.
- Repeat this process to improve the solution.

### Kruskal's Minimum Spanning Tree Algorithm

Another approach implemented is similar to Kruskal's Minimum Spanning Tree algorithm. The steps are as follows:
- From the set of all possible edges, select the shortest edge and add it to a graph while checking for cycles.
- If adding an edge creates a cycle, skip that edge and move to the next shortest edge.
- Continue this process until all edges are exhausted or a limiting condition is reached (number of edges equals number of vertices).