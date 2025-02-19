# CarSharing_RicercaOperativa

## Overview

This project aims to optimize carpooling routes for individuals traveling to the Polo Scientifico Tecnologico UniFe. The goal is to minimize the total distance traveled by cars, considering that each car can carry up to 5 people (including the driver). The project explores various optimization algorithms to achieve this goal.

## Problem Statement

Given the locations of individuals who travel daily to the Polo Scientifico Tecnologico UniFe, the objective is to determine the optimal carpooling routes that minimize the total distance traveled by all cars. Drivers are available to operate the carpooling service, while others prefer to travel as passengers. If no driver serves a passenger, they will drive alone without taking any other passengers.

## Optimization Algorithms

### Clustering Algorithms (K-Means, DBSCAN, Agglomerative Clustering)

**Idea:** Before assigning drivers, passengers are grouped into clusters based on geographical distance. Each cluster should have a maximum of 5 people (including the driver).

**Advantage:** Avoids inefficient routes caused by local greedy decisions.

**Implementation:**
- Execute K-Means with K equal to the number of available drivers.
- Alternatively, use DBSCAN to group passengers based on the density of their locations.
- Assign a driver to each cluster and find the minimum route to pick up all passengers before reaching the Polo.

### Minimum Spanning Tree (MST) Problem

**Idea:** Create a complete graph where each node represents a person, and the edge weights represent the distances between them. Construct a Minimum Spanning Tree (MST) using Prim's or Kruskal's algorithm. Divide the tree into subgroups (each with a maximum of 5 people) and assign a driver to each subgroup.

**Advantage:** Minimizes the sum of distances needed to collect passengers.

**Implementation:**
- Create a complete graph with distances as weights.
- Apply Prim/Kruskal to find the MST.
- Divide the MST into groups of up to 5 nodes using a "pruning" technique and assign a driver to each group.

### Capacitated Traveling Salesman Problem (TSP)

**Idea:** Treat each driver as a traveling salesman who must visit up to 4 passengers before arriving at the Polo. Solve a Capacitated TSP to find the minimum route for each car.

**Advantage:** Optimizes each route to reduce the distance.

**Implementation:**
- Use heuristic algorithms for TSP (e.g., Nearest Neighbor with improvements like 2-opt).
- Use Gurobi or Google OR-Tools for the exact version.

### Simulated Annealing or Genetic Algorithms

**Idea:** Generate a random solution and iteratively improve it by swapping passengers between cars or modifying routes.

**Advantage:** Suitable for complex problems when exact solutions are computationally expensive.

**Implementation:**
- Define a cost function (total distance traveled).
- Use Simulated Annealing to explore solutions near the current one, accepting temporary deteriorations to avoid local minima.
- Alternatively, use Genetic Algorithms with chromosomes representing passenger-to-car assignments.

## Project Structure