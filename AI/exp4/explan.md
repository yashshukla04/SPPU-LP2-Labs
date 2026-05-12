Code Explanation
1. N Variable
int N;

Stores size of chessboard.

2. isSafe()
boolean isSafe(...)

Checks whether queen can be placed safely.

Checks:

column,
left diagonal,
right diagonal.
3. solve()
boolean solve(int[][] board, int row)

Recursive function for placing queens.

4. Base Condition
if (row == N)

If all queens placed:
→ solution found.

5. Place Queen
board[row][col] = 1;

Places queen.

6. Backtracking
board[row][col] = 0;

Removes queen if solution fails.

7. printBoard()

Prints final chessboard solution.

Output

According to output screenshot on page 5:

. Q . .
. . . Q
Q . . .
. . Q .


code explan : B branch and bound 
Branch and Bound Explanation
cols[]

Tracks occupied columns.

diag1[]

Tracks left diagonals.

diag2[]

Tracks right diagonals.

Faster Checking

Instead of scanning board repeatedly:

arrays provide direct checking,
improving efficiency.
Complexity Analysis
Backtracking
Time Complexity:
O(N!)
Branch and Bound

More optimized than pure backtracking.

Viva Questions
What is N-Queens problem?

Problem of placing N queens safely on chessboard.

What is Backtracking?

Recursive technique that tries and reverses choices.

What is Branch and Bound?

Optimization technique reducing unnecessary searches.

Why diagonals are checked?

Queens attack diagonally.

Applications of N-Queens?
Scheduling
Constraint satisfaction
AI search problems
Conclusion

Thus, we successfully implemented N-Queens problem using:

Backtracking,
and Branch & Bound techniques in Java.