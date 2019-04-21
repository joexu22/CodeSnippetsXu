class XandY {
	interface LambdaFunctions {
		int someFunction(int x, int y);
	}

	public void javaOutputs(LambdaFunctions func) {
		int x = 0;
		int y = 0;
		while (x < 10) {
			func.someFunction(x, y);
			System.out.print(x + "" + y + " ");
			x = x + 1;
		}
	}

	public static void main(String[] args) {
		// Can't Do Assignments With Lambda Functions...
		LambdaFunctions A = (x, y) -> y = x - y;
		LambdaFunctions B = (x, y) -> y = y + x;
		// LambdaFunctions C = (x, y) -> {y = y + 2; if ()};
		// LambdaFunctions D = (x, y) -> 2 * (x + y);
		// LambdaFunctions E = (x, y) -> (x + y) ^ 2;
		XandY Solution = new XandY();
		Solution.javaOutputs(A);
		Solution.javaOutputs(B);
	}
}
