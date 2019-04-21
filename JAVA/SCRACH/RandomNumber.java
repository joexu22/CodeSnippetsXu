import java.util.Random;

class RandomNumber {
	public static void main(String[] args) {
		Random rand = new Random();
		int number = rand.nextInt(9) + 1;
		System.out.println(number);
	}
}