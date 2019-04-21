// Understanding pass by reference here...

public class Baby {
	String name;

	Baby(String myname) {
		name = myname;
	}

	Baby() {
	}

	void doSomething(int x, int[] ys, Baby b) {
		x = 99;
		ys[0] = 99;
		b.name = "99";
	}

	public static void main(String[] args) {
		int i = 0;
		int[] j = { 0 };
		Baby k = new Baby("50");
		Baby Solution = new Baby();
		Solution.doSomething(i, j, k);
		System.out.println(i); //0 because it is a primative
		System.out.println(j[0]); //99
		System.out.println(k.name); //99
	}
}