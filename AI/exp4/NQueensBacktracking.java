package AI.exp4;

    public class NQueensBacktracking {

    int N;

    public NQueensBacktracking(int N) {
        this.N = N;
    }

    // Check if safe to place queen
    boolean isSafe(int[][] board,
                   int row,
                   int col) {

        // Check column
        for (int i = 0; i < row; i++) {

            if (board[i][col] == 1)
                return false;
        }

        // Check left diagonal
        for (int i = row - 1,
                 j = col - 1;

             i >= 0 && j >= 0;

             i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        // Check right diagonal
        for (int i = row - 1,
                 j = col + 1;

             i >= 0 && j < N;

             i--, j++) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    boolean solve(int[][] board,
                  int row) {

        if (row == N)
            return true;

        for (int col = 0;
             col < N;
             col++) {

            if (isSafe(board,
                       row,
                       col)) {

                board[row][col] = 1;

                if (solve(board,
                          row + 1))

                    return true;

                // Backtrack
                board[row][col] = 0;
            }
        }

        return false;
    }

    void printBoard(int[][] board) {

        for (int[] row : board) {

            for (int cell : row) {

                System.out.print(
                    cell == 1
                    ? "Q "
                    : ". "
                );
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {

        int N = 4;

        NQueensBacktracking obj =
            new NQueensBacktracking(N);

        int[][] board =
            new int[N][N];

        if (obj.solve(board, 0)) {

            obj.printBoard(board);

        } else {

            System.out.println(
                "No solution exists");
        }
    }
}