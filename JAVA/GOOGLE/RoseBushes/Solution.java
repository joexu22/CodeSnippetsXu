// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
	public int[] checkGroup(boolean[] b) {
		int LongSize = Integer.MAX_VALUE;
		int CurrGroupSize = 0;
		int GroupCount = 0;
		boolean inGroup = false;
		for (int i = 0; i < b.length; i++) {
			if (b[i] == true) {
				if (inGroup) {
					CurrGroupSize++;
				} else {
					inGroup = true;
					CurrGroupSize = 1;
					GroupCount++;
				}
			}
			if (b[i] == false || i == b.length-1) {
				if (inGroup) {
					LongSize = Math.min(LongSize, CurrGroupSize);
					CurrGroupSize = 0;
					inGroup = false;
				} else {
					continue;
				}
			}
		}
		int[] Res = {LongSize, GroupCount};
		return Res;
	}
	 
    public int solution(int[] A, int K, int M) {
		// write your code in Java SE 8
		// K = long, M = groups
		boolean[] test = new boolean[A.length];
		int[] LandG;
		Arrays.fill(test, false);
		// Filling Out The Array In Order...
		for (int j=1; j<=A.length; j++) {
			for (int i = 0; i<A.length; i++) {
				if (A[i] == j) {
					test[i] = true;
				}
			}
			//System.out.println(Arrays.toString(test));
			LandG = checkGroup(test);
			//System.out.println("Group: "+Arrays.toString(LandG));
			if (K == LandG[0] && M == LandG[1]) {
				// System.out.println(LandG[0]+" "+LandG[1]);
				return j;
			}
		}
        return -1;
	}
	
	public static void main(String[] args) {
		int[] input = {1,2,7,3,4,6,5};
		Solution Answer = new Solution();
		int res;
		res = Answer.solution(input, 1, 3); //expect 5
		System.out.println(res);
		res = Answer.solution(input, 7, 1); //expect 7
		System.out.println(res);

		int[] input2 = {1,2,3,10,4,8,6,11,7,5,9};
		res = Answer.solution(input2, 3, 3); //expect 9
		System.out.println(res);
	}
}