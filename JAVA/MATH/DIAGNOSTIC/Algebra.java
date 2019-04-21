class Algebra {
	// ... Make Iterating Letters
	static char lettering = 'a';

	void iterCounter(int n) {
		int i = 0;
		while (i < n) {
			System.out.println(lettering);
			lettering++;
			i++;
		}
	}

	void iterReset() {
		lettering = 'a';
	}
	
	void problemSet1() {
		// Recognize Solution Set For Mathamatics
		double answer;
		answer = Math.pow(-3, 4);
		System.out.println("a: " + answer);
		answer = Math.pow(-3, 4);
		System.out.println("b: " + answer);
		answer = Math.pow(3, -4);
		System.out.println("c: " + answer);
		answer = (double)Math.pow(5, 23)/(double)Math.pow(5, 21);
		System.out.println("d: " + answer);
		answer = Math.pow((2.0/3.0), -2);
		System.out.println("e: " + answer);
		answer = Math.pow(16, (-3.0/4.0));
		System.out.println("f: " + answer);
	}

	public static void main(String[] args) {
		Algebra Solution = new Algebra();
		Solution.problemSet1();
	}
}