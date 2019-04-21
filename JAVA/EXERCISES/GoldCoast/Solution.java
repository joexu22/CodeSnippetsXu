// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
		
		boolean[] counterArray = new boolean[A.length];

		for (int i = 0; i < A.length; i++) {
			if (A[i] > 0 && A[i] <= A.length) {
				counterArray[A[i]-1] = true;
			}
		}

		for(int i = 0; i < counterArray.length; i++) {
			if (counterArray[i] == false) {
				return i+1;
			}
		}

        return A.length + 1;
    }
}