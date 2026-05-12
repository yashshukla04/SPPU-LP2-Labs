Experiment 3
Title

Implementation of Selection Sort, Prim’s Algorithm, and Dijkstra’s Algorithm using Python

Based on your uploaded Experiment 3 file

Aim

To implement:

Selection Sort,
Prim’s Minimum Spanning Tree Algorithm,
and Dijkstra’s Shortest Path Algorithm using Python.
Objectives
To understand greedy algorithms.
To perform sorting using Selection Sort.
To find Minimum Spanning Tree using Prim’s Algorithm.
To find shortest path using Dijkstra’s Algorithm.
Theory
1. Selection Sort

Selection Sort is a simple sorting algorithm.

Working:

Find minimum element from unsorted array.
Swap it with current position.
Repeat until array becomes sorted.

It divides array into:

sorted part
unsorted part
Advantages
Simple implementation
Easy to understand
Requires less memory
Complexity
Time Complexity:
O(n
2
)
Space Complexity:
O(1)
2. Prim’s Minimum Spanning Tree Algorithm

Prim’s Algorithm is a greedy algorithm used to find:

Minimum Spanning Tree (MST)

in weighted undirected graph.

Minimum Spanning Tree:

connects all vertices
minimum total edge weight
no cycles

Prim’s Algorithm:

starts from one node
repeatedly selects minimum weighted edge
Applications
Network design
Cable connections
Road networks
Electrical circuits
Complexity
Time Complexity:
O(V
2
)
3. Dijkstra’s Shortest Path Algorithm

Dijkstra’s Algorithm finds shortest path from source node to all other nodes in weighted graph.

It uses:

Greedy approach
Priority Queue / Min Heap

Working:

Select minimum distance node.
Update distances of neighboring nodes.
Applications
GPS navigation
Routing protocols
Network optimization
Maps
Complexity
Time Complexity:
O((V+E)logV)
Algorithm
Selection Sort Algorithm
1. Find minimum element.
2. Swap with current position.
3. Move to next position.
4. Repeat until array sorted.
Prim’s Algorithm
1. Start from source node.
2. Select minimum weighted edge.
3. Add edge to MST.
4. Repeat until all vertices included.
Dijkstra’s Algorithm
1. Initialize distances.
2. Select minimum distance node.
3. Update neighboring distances.
4. Repeat until all nodes visited.