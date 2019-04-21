
class StringCompression {
	public String solution(String str) {
		StringBuilder out = new StringBuilder();
		int counter = 0;
		for (int i = 0; i < str.length(); i++) {
			counter++;
			if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i+1)) {
				out.append(str.charAt(i));
				out.append(counter);
				counter = 0;
			}
		}
		return out.length() < str.length() ? out.toString() : str;
	}

	public static void main(String[] args) {
		String test = "aabcccccaaa";
		StringCompression Solution = new StringCompression();
		System.out.println(Solution.solution(test));
	}
}