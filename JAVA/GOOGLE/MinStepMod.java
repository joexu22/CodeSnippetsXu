
/*
Given start, end and an array of N numbers.
At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.
The task is to find the minimum steps in which end can be achieved starting from start.

E.G.
    Input: start = 3 end = 30 a[] = {2, 5, 7}
    Output: 2
    Step 1: 3*2 = 6 % 100000 = 6
    Step 2: 6*5 = 30 % 100000 = 30

    Input: start = 7 end = 66175 a[] = {3, 4, 65}
    Output: 4
    Step 1: 7*3 = 21 % 100000 = 21
    Step 2: 21*3 = 6 % 100000 = 63
    Step 3: 63*65 = 4095 % 100000 = 4095
    Step 4: 4095*65 = 266175 % 100000 = 66175 
*/

import java.util.*;

class MinStepMod {
    // One needs to use a queue for this solution
    // Interesting Concept - I was thinking about recursion, but a queue stops the recurrence
    public int solution(int start, int end, int[] array) {
        int TABLE_SIZE = 100001;
        int mod = 100000;
        int[] table = new int[TABLE_SIZE];
        Arrays.fill(table, -1);

        // Queue is an interface and it is neccessary to use instantiate it as linked list
        Queue<Integer> q = new LinkedList<>();

        q.add(start % mod);
        table[start] = 0;

        while (!q.isEmpty()) {
            int top = q.peek();
            q.remove();
            if (top == end) {
                return table[end];
            }

            for (int i = 0; i < array.length; i++) {
                int pushed = top * array[i];
                pushed = pushed % mod;

                if (table[pushed] == -1) {
                    table[pushed] = table[top] + 1;
                    q.add(pushed);
                }
            }

        }
        return -1;
    }

    public static void main(String[] args) {
        int start;
        int end;
        int[] a;

        start = 3;
        end = 30;
        a = new int[] { 2, 5, 7 };
        MinStepMod answer = new MinStepMod();
        int out = answer.solution(start, end, a);
        System.out.println(out);

        start = 7;
        end = 66175;
        a = new int[] { 3, 4, 65 };
        out = answer.solution(start, end, a);
        System.out.println(out);

    }
}