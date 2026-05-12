Experiment 2
Title

Implementation of A* Algorithm for 8 Puzzle Problem using Java

Aim

To implement A* Algorithm for solving the 8-puzzle problem using informed search technique.

Objectives
To understand informed search algorithms.
To implement A* search algorithm.
To solve the 8-puzzle problem using heuristic function.
Theory
Introduction to A* Algorithm

A* (A-Star) is one of the most efficient informed search algorithms used in Artificial Intelligence for:

path finding,
graph traversal,
and game search problems.

A* uses:

actual path cost
heuristic estimated cost

to determine the optimal path.

Evaluation Function

A* uses evaluation function:

f(n)=g(n)+h(n)

Where:

g(n) = actual cost from start node
h(n) = heuristic cost to goal node
f(n) = total estimated cost
Heuristic Function

In 8-puzzle problem:

heuristic = number of misplaced tiles.

A* selects node with minimum f(n) value.

8 Puzzle Problem

The 8-puzzle consists of:

8 numbered tiles
1 blank space represented by 0

Goal:
Arrange tiles from initial state to goal state.

Initial State
1 2 3
4 0 6
7 5 8
Goal State
1 2 3
4 5 6
7 8 0
Advantages of A*
Efficient searching
Faster than uninformed search
Uses heuristic intelligence
Finds near optimal solution
Applications
GPS navigation
Robot motion planning
Video games
Puzzle solving
Route optimization
Algorithm
1. Create OPEN list and CLOSED list.
2. Insert initial state into OPEN list.
3. Select node with minimum f(n).
4. Remove node from OPEN list.
5. Add node into CLOSED list.
6. If goal state reached, stop.
7. Generate neighboring states.
8. Calculate heuristic values.
9. Insert valid states into OPEN list.
10. Repeat until goal state is reached.


Complexity Analysis
Time Complexity:
Exponential in worst case
Space Complexity:
High due to state storage