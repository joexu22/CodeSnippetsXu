class OneAway {
	boolean OneAwayBruteForce(String A, String B) {
		int size_diff = Math.abs(A.length() - B.length());
		if (size_diff > 1) {
			return false;
		}
		String big;
		String small;
		if (A.length() > B.length()) {
			big = A;
			small = B;
		} else {
			big = B;
			small = A;
		}
		// insert
		int index1 = 0;
		int index2 = 0;
		boolean insert = false;
		while (index1 < big.length() && index2 < small.length()) {
			if (big.charAt(index1) != small.charAt(index2)) {
				if (insert) {
					return false;
				} else {
					insert = true;
					index1++;
				}
			}
			index1++;
			index2++;
		}
		return true;
		// remove
		// replace
	}
	public static void main(String[] args) {
		String sText = "bb";
		String bText = "abb";

		OneAway Solution = new OneAway();
		boolean out = Solution.OneAwayBruteForce(sText, bText);
		System.out.println(out);
	}
}