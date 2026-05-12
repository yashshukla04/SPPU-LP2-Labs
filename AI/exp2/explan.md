Code Explanation
1. Import Package
import java.util.*;

Imports utility classes:

PriorityQueue
ArrayList
HashSet
2. State Class
class State

Represents each puzzle state.

Stores:

board
g(n)
h(n)
f(n)
parent node
3. Heuristic Function
static int heuristic(int[][] board)

Counts misplaced tiles.

Returns heuristic value h(n).

4. Goal State
static int[][] goal

Defines final desired puzzle arrangement.

5. printBoard()
static void printBoard(int[][] board)

Prints puzzle board.

6. getNeighbors()
static List<int[][]> getNeighbors(int[][] board)

Generates possible moves:

up
down
left
right

by moving blank tile.

7. Priority Queue
PriorityQueue<State> open

Stores states based on minimum f(n).

8. OPEN and VISITED
Set<String> visited

Prevents revisiting same states.

9. Goal Check
if (current.h == 0)

If heuristic becomes 0:
→ goal state reached.

10. printSolution()

Prints:

start state
intermediate states
goal state