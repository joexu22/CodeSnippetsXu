import java.util.Random;

class RandomNumber {
	public static int singleNumber() {
		Random rand = new Random();
		int number = rand.nextInt(9) + 1;
		return number;
	}

	public static void main(String[] args) {
		System.out.println(singleNumber());
	}
}

