import java.util.*;

class State {
    int[][] board;
    int g;
    int h;
    int f;
    State parent;

    State(int[][] board, int g, State parent) {
        this.board = board;
        this.g = g;
        this.h = heuristic(board);
        this.f = g + h;
        this.parent = parent;
    }

    static int heuristic(int[][] board) {
        int[][] goal = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 0}
        };

        int count = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] != 0 &&
                    board[i][j] != goal[i][j]) {
                    count++;
                }
            }
        }

        return count;
    }
}

public class AStar {

    static int[][] goal = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    static void printBoard(int[][] board) {

        for (int[] row : board) {

            for (int val : row) {
                System.out.print(val + " ");
            }

            System.out.println();
        }

        System.out.println();
    }

    static List<int[][]> getNeighbors(int[][] board) {

        List<int[][]> neighbors =
            new ArrayList<>();

        int x = 0, y = 0;

        for (int i = 0; i < 3; i++) {

            for (int j = 0; j < 3; j++) {

                if (board[i][j] == 0) {
                    x = i;
                    y = j;
                }
            }
        }

        int[][] moves = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        for (int[] m : moves) {

            int nx = x + m[0];
            int ny = y + m[1];

            if (nx >= 0 && ny >= 0 &&
                nx < 3 && ny < 3) {

                int[][] newBoard =
                    new int[3][3];

                for (int i = 0; i < 3; i++) {
                    newBoard[i] =
                        board[i].clone();
                }

                newBoard[x][y] =
                    newBoard[nx][ny];

                newBoard[nx][ny] = 0;

                neighbors.add(newBoard);
            }
        }

        return neighbors;
    }

    static void printSolution(State node) {

        List<int[][]> path =
            new ArrayList<>();

        while (node != null) {
            path.add(node.board);
            node = node.parent;
        }

        Collections.reverse(path);

        System.out.println("Start State:");
        printBoard(path.get(0));

        System.out.println("Goal State:");
        printBoard(goal);

        System.out.println(
            "Steps to reach Goal State:\n");

        for (int i = 1; i < path.size(); i++) {

            System.out.println(
                "Step " + i + ":");

            printBoard(path.get(i));
        }

        System.out.println(
            "Goal State Reached!");
    }

    static void solve(int[][] start) {

        PriorityQueue<State> open =
            new PriorityQueue<>(
                Comparator.comparingInt(a -> a.f)
            );

        Set<String> visited =
            new HashSet<>();

        open.add(new State(start, 0, null));

        while (!open.isEmpty()) {

            State current = open.poll();

            if (current.h == 0) {

                printSolution(current);
                return;
            }

            visited.add(
                Arrays.deepToString(current.board)
            );

            for (int[][] next :
                    getNeighbors(current.board)) {

                if (!visited.contains(
                    Arrays.deepToString(next))) {

                    open.add(
                        new State(
                            next,
                            current.g + 1,
                            current
                        )
                    );
                }
            }
        }

        System.out.println(
            "No solution found.");
    }

    public static void main(String[] args) {

        int[][] start = {
            {1, 2, 3},
            {4, 0, 6},
            {7, 5, 8}
        };

        solve(start);
    }
}