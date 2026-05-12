Code Explanation A: selection sort
len(arr)
n = len(arr)

Stores size of array.

Outer Loop
for i in range(n):

Traverses entire array.

Find Minimum Element
if arr[j] < arr[min_idx]:

Checks smaller element.

Swap Elements
arr[i], arr[min_idx] = arr[min_idx], arr[i]

Places smallest element in correct position.

Output

According to output screenshot on page 3:

Sorted array:
[11, 12, 22, 25, 64]





Code Explanation B: prims
heapq
import heapq

Used for priority queue.

Min Heap
min_heap = [(0, start, -1)]

Stores:

edge weight
current node
parent node
Visited Set
visited = set()

Avoids revisiting nodes.

Select Minimum Edge
heapq.heappop(min_heap)

Extracts minimum weighted edge.

Add Edge to MST
mst.append((parent, node, cost))

Adds edge into spanning tree.

Output

From output screenshot on page 3:

MST:
[(0,1,2), (1,2,3),
 (1,4,5), (0,3,6)]

Total Cost: 16


code Explanation C: dijkstra's
Initialize Distances
dist = {node: float('inf')}

Initially all distances are infinity.

Source Distance
dist[start] = 0

Distance of source node is 0.

Priority Queue
min_heap = [(0, start)]

Stores minimum distance node.

Update Distances
if distance < dist[neighbor]:

Updates shorter path.

Output

According to screenshot on page 3:

Shortest distances:
{'A': 0, 'B': 1,
 'C': 3, 'D': 4}