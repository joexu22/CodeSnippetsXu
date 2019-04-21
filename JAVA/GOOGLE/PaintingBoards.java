class PaintingBoards {
    public int sum(int[] A, int from, int to) {
        int total = 0;
        for (int i = from; i <= to; i++) {
            total += A[i];
        }
        return total;
    }

    public int partition(int k, int n, int[] A) {
        if (k == 1) {
            return sum(A, 0, n - 1);
        }
        if (A.length == 1) {
            return A[0];
        }

        int best = Integer.MAX_VALUE;
        for (int i = 0; i <= n; i++) {
            // This part involves pure mathamatics
            best = Math.min(best, Math.max(partition(k - 1, i, A), sum(A, i, n - 1)));
        }
        return best;
    }

    public int dynamicPartition(int[] A, int n, int k) {
        int[][] table = new int[k + 1][n + 1];
        // Base Cases
        // k=1
        for (int i = 0; i <= n; i++) {
            table[1][i] = sum(A, 0, i - 1);
        }
        // n=1
        for (int i = 0; i <= k; i++) {
            table[i][1] = A[0];
        }
        for (int i = 2; i <= k; i++) {
            for (int j = 2; j <= n; j++) {
                // track minimum
                int best = Integer.MAX_VALUE;
                // i-1 th separator before position arr[p=1..j]
                for (int p = 1; p <= j; p++)
                    best = Math.min(best, Math.max(table[i - 1][p], sum(A, p, j - 1)));

                table[i][j] = best;
            }
        }
        return table[k][n];
    }

    public int solution(int k, int[] A) {
        // return partition(k, A.length, A);
        return dynamicPartition(A, A.length, k);
    }

    public static void main(String[] args) {
        int[] test1 = new int[] { 10, 20, 60, 50, 30, 40 };
        int[] test2 = new int[] { 50 };

        PaintingBoards Solution = new PaintingBoards();

        System.out.println(Solution.solution(1, test1));
        System.out.println(Solution.solution(3, test2));
        System.out.println(Solution.solution(3, test1));
    }
}