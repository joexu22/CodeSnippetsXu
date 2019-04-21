import java.util.Arrays;

class Rotation {
	boolean rotate(int[][] matrix) {
		if (matrix.length == 0 || matrix.length != matrix[0].length) {
			return false;
		}
		int n = matrix.length;
		// Understanding Layers
		for (int layer = 0; layer < n / 2; layer++) {
			int first = layer;
			int last = n - first - 1;
			for (int i = first; i < last; i++) {
				int offset = i - first;
				int top = matrix[first][i];
				matrix[first][i] = matrix[last - offset][first];
				matrix[last - offset][first] = matrix[last][last - offset];
				matrix[last][last - offset] = matrix[i][last];
				matrix[i][last] = top;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		int[][] test = { { 1, 2 }, { 3, 4 } };
		for (int i = 0; i < test.length; i++) {
			System.out.println(Arrays.toString(test[i]));
		}
		int[][] test2 = { { 3, 1 }, { 4, 2 } };
		for (int i = 0; i < test2.length; i++) {
			System.out.println(Arrays.toString(test2[i]));
		}

		Rotation Solution = new Rotation();
		Solution.rotate(test);
		for (int i = 0; i < test.length; i++) {
			System.out.println(Arrays.toString(test[i]));
		}
	}
}