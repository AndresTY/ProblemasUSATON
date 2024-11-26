# Descent Walking Competition Solver

## Problem Description

This problem simulates a competitive descent walking challenge involving three highly competitive friends: Aquiles, Perseo, and Teseo. The challenge takes place on a geographical terrain represented as an n × n grid, where each cell represents the slope or elevation of that specific location.

### Competition Rules

1. **Starting Positions**:
   - Each participant starts at a different position along the northern or western edge of the terrain.
   - No two participants can start at the same location.

2. **Descent Rules**:
   - Participants can only move to an adjacent cell (up, down, left, right) with a slope less than or equal to their current position.
   - Movement priority is determined by a specific set of rules:
     a. First, prefer cells within the immediate neighborhood with a lower or equal slope.
     b. If no such cell exists, look for cells outside the immediate neighborhood with a lower or equal slope.
   - When multiple movement options exist, choose the direction in clockwise order, starting from the north.

3. **Objective**:
   - The goal is to reach the lowest point on the terrain (a cell with value 0).
   - The fastest route (shortest path) to this point is considered the winner.

### Input Format

- First line: Number of test cases (T)
- For each test case:
  - First line: Size of the terrain (n × n)
  - Second line: Six coordinates representing the starting positions of the three participants
  - Next n lines: Terrain elevation matrix

### Output

The program outputs the sequence of slope values for the fastest descent route that reaches the lowest point.

## Solution Approach

The Python solution (`CarreraDeDescenso.py`) implements this challenge through two main functions:

1. `darAscensoCorredor()`:
   - Handles the descent for a single participant
   - Implements the movement rules described in the problem statement
   - Tracks the route and ensures no revisiting of cells
   - Returns the route of slope values

2. `ascendingCompetence()`:
   - Coordinates the descent for all three participants
   - Compares their routes based on:
     a. Reaching the lowest point (value 0)
     b. Route length (shortest path wins)
   - Selects and returns the optimal route

## Example

```
Input:
1
5
0 1 0 4 3 0
9 10 8 8 7 5
9 8 7 5 6 4
7 4 7 6 7 3
6 4 1 4 2 3
5 4 1 2 1 1
4 1 2 1 0 2
6 4 1 1 1 0

Output:
10 8 8 7 7 4 2 0
```

## Key Challenges

- Implementing complex movement rules
- Tracking visited cells
- Comparing routes efficiently
- Handling edge cases where not all participants reach the goal

## Complexity Considerations

- Time Complexity: O(n²), where n is the terrain size
- Space Complexity: O(n²) to store visited cells and route

## Potential Improvements

- Add more robust error handling
- Implement more sophisticated route optimization
- Add visualization of the descent paths
