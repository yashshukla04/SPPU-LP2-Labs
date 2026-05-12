Experiment: DFS and BFS Traversal using Python
Aim

To implement Breadth First Search (BFS) and Depth First Search (DFS) traversal techniques for an undirected graph using Python.

Objectives
To understand graph traversal techniques.
To implement BFS using Queue.
To implement DFS using Recursion.
To traverse all vertices of an undirected graph.

Theory
Introduction to Graph

A graph is a non-linear data structure consisting of:

Vertices (Nodes)
Edges (Connections)

Graphs are used in:

Social networks
Maps and navigation
Computer networks
Web crawling
AI search problems
Breadth First Search (BFS)

Breadth First Search is a graph traversal algorithm that visits nodes level by level.

In BFS:

Start from source node.
Visit all neighboring nodes first.
Then move to next level nodes.

BFS uses:

Queue data structure
FIFO (First In First Out)
Working of BFS

Consider graph:

        A
      /   \
     B     C
    / \     \
   D   E     F

BFS Traversal starting from A:

A → B → C → D → E → F

Explanation:

First visit A
Then neighbors B and C
Then neighbors of B: D and E
Then neighbor of C: F

Applications of BFS
Shortest path finding
GPS navigation
Social networking systems
Web crawlers
Broadcasting systems

BFS Complexity
Time Complexity:
O(V+E)

Space Complexity:
O(V)

Where:

V = Number of vertices
E = Number of edges

Depth First Search (DFS)

Depth First Search is a graph traversal algorithm that explores nodes deeply before backtracking.

In DFS:

Start from source node.
Visit one node completely.
Move deeper into graph.
Backtrack when no unvisited node is available.

DFS uses:

Stack
Or recursion
Working of DFS

Using same graph:

        A
      /   \
     B     C
    / \     \
   D   E     F

DFS Traversal:

A → B → D → E → C → F

Explanation:

Start at A
Go deep into B
Then D
Backtrack to E
Then move to C and F
Applications of DFS
Cycle detection
Path finding
Maze solving
Topological sorting
Connected components
DFS Complexity
Time Complexity:
O(V+E)
Space Complexity:
O(V)
Algorithm
BFS Algorithm
1. Create visited list and queue.
2. Insert starting node into queue.
3. Mark starting node as visited.
4. Remove front node from queue.
5. Print the node.
6. Add all unvisited neighboring nodes into queue.
7. Repeat until queue becomes empty.

DFS Algorithm
1. Start from source node.
2. Mark node as visited.
3. Print node.
4. Visit adjacent unvisited nodes recursively.
5. Repeat until all nodes are visited.