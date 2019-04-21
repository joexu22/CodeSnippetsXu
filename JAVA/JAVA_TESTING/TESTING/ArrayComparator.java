import java.util.*;

class ArrayComparator {
	public static void main(String[] args) {
		int[] testA = {1,2,0};
		int[] testB = {1,2,3};
		int[] testC = {3,3,11};
		int[] testD = {0,1,8};
		int[] testE = {1,8,7};
		int[] testF = {0,4,6};
		
		/*
		TreeSet<int[]> testSet = new TreeSet<int[]>(new Comparator<int[]>() {
			public int compare(int[] a, int[] b) {
				return a[2] - b[2];
			}
		});
		*/

		TreeSet<int[]> testSet = new TreeSet<int[]>(new Comparator<int[]>() {
			@Override
			public int compare(final int[] entry1, final int[] entry2) {
				// Ensures that matrix is sorted by iRow and then iColumn
				if (entry1[1]>entry2[1]) { //sorts by iColumn
					if (entry1[0]>=entry2[0]) { //sorts by iRow, keeping iColumn in place
						return 1;
					} else {
						return -1;
					}
				} else {
					return -1;
				}
			}
		});
		
		testSet.add(testA);
		System.out.println(testSet.size());
		testSet.add(testB);
		System.out.println(testSet.size());
		testSet.add(testC);
		System.out.println(testSet.size());
		testSet.add(testD);
		testSet.add(testE);
		testSet.add(testF);

		HashSet<int[]> newSet = new HashSet<int[]>();
		int[] newA = {0,2,0};
		int[] newB = {1,3,1};
		int[] newC = {2,4,3};
		int[] newD = {3,5,7};
		int[] newE = {4,7,9};
		newSet.add(newA);
		newSet.add(newB);
		newSet.add(newC);
		newSet.add(newD);
		newSet.add(newE);

		for (int[] output : testSet) {
			System.out.println(Arrays.toString(output));
		}
		
		System.out.println("-New Output-");
		//testSet.addAll(newSet);
		testSet.add(newA);   
		testSet.add(newB);   
		testSet.add(newC);   
		testSet.add(newD);   
		testSet.add(newE);
	
		newSet.it
		for (int[] output : testSet) {
			System.out.println(Arrays.toString(output));
		}

	}
}