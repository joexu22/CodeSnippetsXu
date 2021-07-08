import java.util.*;

public class JavaArray {
	List<String> construction = Arrays.asList("CONSTRUCTION");
	List<String> perspective = Arrays.asList("PERSPECTIVE");
	List<String> gesture = Arrays.asList("GESTURE");
	List<String> anatomy = Arrays.asList("ANATOMY");
	List<String> color = Arrays.asList("COLOR");
	List<String> composition = Arrays.asList("COMPOSITION");
	List<String> design = Arrays.asList("DESIGN");

	public static void main(String[] args) {
		JavaArray newJavaArray = new JavaArray();
		char[] characterArray = newJavaArray.construction.get(0).toCharArray();
		Arrays.sort(characterArray);
		System.out.println(characterArray);

		System.out.println(newJavaArray.construction);
		System.out.println(newJavaArray.perspective);
		System.out.println(newJavaArray.gesture);
		System.out.println(newJavaArray.anatomy);
		System.out.println(newJavaArray.color);
		System.out.println(newJavaArray.composition);
		System.out.println(newJavaArray.design);
	}
}
