import java.util.*;

// Given a rod of length L, the task is to cut the rod in such a way that the total number of segments of length p, q, and r is maximized.
// The segments can only be of length p, q, and r.

public class MaximizeLengthDynamic {
    public static class Solution {
        // This was the textbook solution...
        // Rather than build the solution incrementally for each possible length, it builds the solution with each possible added segment
        public int[] solution(int L, int p, int q, int r) {
            int[] table = new int[L + 1];
            Arrays.fill(table, -1);
            table[0] = 0;
            
            for (int i = 0; i <= L; i++) {
                if (table[i] == -1) {
                    continue;
                }
                if (i + p <= L) {
                    table[i + p] = Integer.max(table[i + p], table[i] + 1);
                }
                if (i + q <= L) {
                    table[i + q] = Integer.max(table[i + q], table[i] + 1);
                }
                if (i + r <= L) {
                    table[i + r] = Integer.max(table[i + r], table[i] + 1);
                }
            }
            return table;
        }

        // This solution was an first attempt...
        // It has logical mistakes that are filled in by pratical hacks
        public int[] solution2(int L, int p, int q, int r) {
            // The Approach is to build a dynamic solution for each possible length, incrementing upwards...
            int[] table = new int[L + 1]; // Basis of Dynamic Programming
            Arrays.fill(table, Integer.MIN_VALUE);
            int min_index = Integer.min(Integer.min(p, q), r);
            table[0] = 0;
            table[min_index] = 1;
        
            for (int i = 0; i <= L; i++) {
                if (i - p >= 0) {
                    if (table[i - p] == Integer.MIN_VALUE) {
                        continue;
                    }
                    table[i] = Integer.max(table[i], table[i - p] + 1);
                }
                if (i - q >= 0) {
                    if (table[i - q] == Integer.MIN_VALUE) {
                        continue;
                    }
                    table[i] = Integer.max(table[i], table[i - q] + 1);
                }
                if (i - r >= 0) {
                    if (table[i - r] == Integer.MIN_VALUE) {
                        continue;
                    }
                    table[i] = Integer.max(table[i], table[i - r] + 1);
                }
            }
            return table;
        }
    }

    public static void main(String[] args) {
        Solution answer = new Solution();
        int[] out = answer.solution(7, 2, 5, 5);
        for (int i = 0; i < out.length; i++) {
            System.out.println(out[i]);
        }
        System.out.println("--------------------------------------------");
        int[] out2 = answer.solution2(20, 2, 5, 1);
        for (int i = 0; i < out2.length; i++) {
            System.out.println(out2[i]);
        }

    }
}