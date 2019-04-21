import java.util.Arrays;

class SwapLetter {
	boolean canTransform(String A, String B) {
		if (A.length() != B.length()) {
			return false;
		}
		char[] Astr = A.toCharArray();
		char[] Bstr = B.toCharArray();
		// {L, R, X}
		int[] counterA = { 0, 0, 0 };
		int[] counterB = { 0, 0, 0 };
		for (int i = 0; i < Astr.length; i++) {
			if (Astr[i] == 'L') {
				counterA[0]++;
			} else if (Astr[i] == 'R') {
				counterA[1]++;
			} else if (Astr[i] == 'X') {
				counterA[2]++;
			} else {
				return false;
			}
		}
		for (int i = 0; i < Bstr.length; i++) {
			if (Bstr[i] == 'L') {
				counterB[0]++;
			} else if (Bstr[i] == 'R') {
				counterB[1]++;
			} else if (Bstr[i] == 'X') {
				counterB[2]++;
			} else {
				return false;
			}
		}
		if (!Arrays.equals(counterA, counterB)) {
			return false;
		}
		System.out.println(Arrays.toString(counterA));
		System.out.println(Arrays.toString(counterB));

		StringBuilder sbA = new StringBuilder();
		StringBuilder sbB = new StringBuilder();
		for (int i = 0; i < A.length(); i++) {
			if (A.charAt(i) != 'X') {
				sbA.append(A.charAt(i));
			}
		}
		for (int i = 0; i < B.length(); i++) {
			if (B.charAt(i) != 'X') {
				sbB.append(B.charAt(i));
			}
		}
		// return sbA.toString().equals(sbB.toString());

		int indexA = 0;
		int indexB = 0;
		while (indexA < Astr.length && indexB < Bstr.length) {
			while (Astr[indexA] == 'X') {
				indexA++;
			}
			while (Bstr[indexB] == 'X') {
				indexB++;
			}
			if (Astr[indexA] != Bstr[indexB]) {
				return false;
			}
			indexA++;
			indexB++;
		}
		return true;
		// Rubbish Implementation...
		// int indxA = 0;
		// int indxB = 0;
		// for (int i = 0; i < Astr.length; i++) {
		// while (Astr[indxA] == 'X') {
		// if (indxA < Astr.length-1) {
		// indxA++;
		// }
		// }
		// while (Bstr[indxB] == 'X') {
		// if (indxB < Bstr.length-1) {
		// indxB++;
		// }
		// }
		// if (Astr[indxA] != Bstr[indxB]) {
		// return false;
		// }
		// if (indxA < Astr.length-1) {
		// indxA++;
		// }
		// if (indxB < Bstr.length-1) {
		// indxB++;
		// }
		// }
		// return true;
	}

	public static void main(String[] args) {
		// Testing Array Compare
		int[] counterA = { 0, 0, 0 };
		int[] counterB = { 0, 0, 0 };
		System.out.println(Arrays.equals(counterA, counterB)); // Array Compare

		// Function
		String start = "RXXLRXRXL";
		String end = "XRLXXRRLX";
		SwapLetter Solution = new SwapLetter();
		boolean out = Solution.canTransform(start, end);
		System.out.println(out);
		
		String A1 = "RRXXLLXXXRLXLR";
		String A2 = "RXRXLXXXLRXLLR";
		out = Solution.canTransform(A1, A2);
		System.out.println(out);

		A1 = "RLXXLLXXXRLXLR";
		A2 = "RXRXLXLXLRXLLR";
		out = Solution.canTransform(A1, A2);
		System.out.println(out);

	}
}