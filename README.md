# CarSharing RicercaOperativa

## Overview

This project aims to optimize carpooling routes for individuals traveling to the Polo Scientifico Tecnologico UniFe. The goal is to minimize the total distance traveled by cars, considering that each car can carry up to 5 people (including the driver). The project explores various optimization algorithms to achieve this goal.

## Problem Statement

Given the locations of individuals who travel daily to the Polo Scientifico Tecnologico UniFe, the objective is to determine the optimal carpooling routes that minimize the total distance traveled by all cars. Drivers are available to operate the carpooling service, while others prefer to travel as passengers. If no driver serves a passenger, they will drive alone without taking any other passengers.

## Greedy Algorithms

### Greedy 1 Algorithm

**Idea:**

Each driver picks up the nearest passenger until the car is full. This approach ensures that the carpooling routes are as short as possible by always selecting the closest passenger, thereby minimizing the additional distance traveled for each pickup. This greedy strategy is simple and efficient, making it a good starting point for route optimization.

**Implementation:**

For each driver, a function is used to calculate the nearest passenger among all users, in terms of Euclidean distance. Once the nearest passenger is found, the driver moves to its location, and the calculation is repeated from that point. The algorithm terminates when the driver's car is full, and then they can proceed to the destination.

### Greedy 2 Algorithm

**Idea:** 

The basic idea is the same as the Greedy 1 algorithm, but changes the method for evaluating which passenger is most convenient to pick up before reaching the destination. In this method, the distance between the driver and the passenger and the distance between the passenger and the destination are evaluated.

**Implementation:**

For each driver, a function is used to calculate the nearest passenger among all users. The distance is calculate using the formula:

$$ dist = \frac{k \cdot d_{D-U}}{d_{U-P}}$$

where:
- $k$ is a parameter used to add weight to the distance $d_{D-U}$
- $d_{D-U}$ is the Euclidean Distance between the driver and the user
- $d_{U-P}$ is the Euclidean Distance between the user and the polo

Once the nearest passenger is found, the driver moves to its location, and the calculation is repeated from that point. The algorithm terminates when the driver's car is full, and then they can proceed to the destination.

### Greedy Results

![ResultGreedy](https://github.com/user-attachments/assets/49ae1815-7f5b-4c14-9d07-457badb15634)

## Constructive Greedy Algorithms

### K-Means 1 Algorithm

**Idea:** 

This algorithm uses clustering techniques to optimize the routes taken by drivers. The algorithm used is K-Means, which, starting from the drivers' positions, finds the nearest users in terms of Euclidean distance and adds them to the same cluster. Once the clusters are obtained, the route is created by finding the four nearest neighbors of the driver.

**Implementation:**

For this algorithm, we used the sklearn library, which provides the implementation of the K-Means algorithm. The centroids are initialized at the drivers' positions, and the algorithm iterates by modifying the centroids' positions and assigning users to clusters until it reaches a stable state where no further changes are made. Once the final clusters are obtained, starting from the driver, the route is created using an algorithm that finds the four nearest neighbors of the driver, that belong to the same cluster.

### K-Means 2 Algorithm

**Idea:** 

This algorithm uses the same K-Means algorithm described in K-Means 1 but once the clusters are obtained, the route is created using the distance algorithm also used in Greedy 2.

**Implementation:**

Also for this algorithm the centroids are initialized at the drivers' positions, and the algorithm iterates by modifying the centroids' positions and assigning users to clusters until it reaches a stable state where no further changes are made. Once the final clusters are obtained, starting from the driver, the route is created using the formula described in Greedy 2, which considers both the distance between the driver and the passenger and the distance between the passenger and the destination.

### K-Means Results

![ResultKMeans](https://github.com/user-attachments/assets/d12875c9-84e2-474c-9919-0bcd0f8437ff)

## Local Search Algorithms

### Local Search 1 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Local Search 1 Results

![ResultLocalSearch1](https://github.com/user-attachments/assets/20922a68-ed32-461f-8f3a-6c0dbc9bdc3d)

### Local Search 2 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Local Search 2 Results

![ResultLocalSearch2](https://github.com/user-attachments/assets/a618270d-7574-423b-88be-acd6d0051fe4)

### Local Search 3 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Local Search 3 Results

![ResultLocalSearch3](https://github.com/user-attachments/assets/693225ce-4d86-4fec-8aa5-116668e8dd00)

## Multi Start Local Search Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Multi Start Local Search Results

![ResultMultiStartLocalSearch](https://github.com/user-attachments/assets/c1df94fa-7459-4f25-9374-883ed717b30e)

## Project Structure
