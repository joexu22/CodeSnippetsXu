public class JavaArrayMutation {
    private int[] testArray = {5, 26, 2021};
    
	// This does not save
    public void increment(int n) {
        n++;
	}
	
	// This saves the number
	public int set_one_higher(int n) {
		return ++n;
	}
    
    public void firstTestMethod() {
        for (int i = 0; i < testArray.length; i++) {
            increment(testArray[i]);
            System.out.print(testArray[i] + " ");
        }
    }

    public void secondTestMethod() {
        for (int element : testArray) {
            increment(element);
            System.out.print(element + " ");
        }
    }

	public void thirdTestMethod() {
		for (int i = 0; i < testArray.length; i++) {
			testArray[i] = set_one_higher(testArray[i]);
			//testArray[i] = 4;
			System.out.print(testArray[i] + " ");
		}
	}

    public static void main(String[] args) {
        JavaArrayMutation A = new JavaArrayMutation();
		A.firstTestMethod();
		System.out.println();
		
		JavaArrayMutation B = new JavaArrayMutation();
        B.secondTestMethod();
		System.out.println();

		JavaArrayMutation C = new JavaArrayMutation();
        C.thirdTestMethod();
		System.out.println();
    }
}
