# CarSharing_RicercaOperativa

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
The basic idea is the same as the Greedy 1 algorithm, but the method for evaluating which passenger is most convenient to pick up before reaching the destination changes. In this method, the distance between the driver and the passenger and the distance between the passenger and the destination are evaluated.

**Implementation:**
For each driver, a function is used to calculate the nearest passenger among all users. The distance is calculate using the formula:
$$dist = \frac{k \: d_{D-U}}{d_{U-P}}$$
where:
$d_{D-U}$ is the Eculidean Distance between the driver and the user, 
$d_{D-U}$ is the Eculidean Distance between the user and the polo and
$k$ is a parameter used to add weight to the distance $d_{D-U}$.
Once the nearest passenger is found, the driver moves to its location, and the calculation is repeated from that point. The algorithm terminates when the driver's car is full, and then they can proceed to the destination.

## Constructive Greedy Algorithms

### K-Means 1 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### K-Means 2 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

## Local Search Algorithms

### Local Search 1 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Local Search 2 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

### Local Search 3 Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

## Multi Start Local Search Algorithm

**Idea:** Lorem Ipsum

**Implementation:**
- Lorem Ipsum
- Lorem Ipsum
- Lorem Ipsum

## Project Structure