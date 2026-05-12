package AI.exp4;

    public class NQueensBranchBound {

    int N;

    boolean[] cols;
    boolean[] diag1;
    boolean[] diag2;

    public NQueensBranchBound(int N) {

        this.N = N;

        cols = new boolean[N];
        diag1 = new boolean[2 * N];
        diag2 = new boolean[2 * N];
    }

    boolean solve(int[][] board,
                  int row) {

        if (row == N)
            return true;

        for (int col = 0;
             col < N;
             col++) {

            if (!cols[col] &&
                !diag1[row + col] &&
                !diag2[row - col + N]) {

                board[row][col] = 1;

                cols[col] =
                diag1[row + col] =
                diag2[row - col + N]
                = true;

                if (solve(board,
                          row + 1))

                    return true;

                // Backtrack
                board[row][col] = 0;

                cols[col] =
                diag1[row + col] =
                diag2[row - col + N]
                = false;
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

        NQueensBranchBound obj =
            new NQueensBranchBound(N);

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
