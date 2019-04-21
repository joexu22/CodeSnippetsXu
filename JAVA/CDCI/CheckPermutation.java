import java.util.Arrays;

class CheckPermutation {
    public boolean solution(String S1, String S2) {
        if (S1.length() != S2.length()) {
            return false;
        }

        int NUM = Character.MAX_VALUE;
        int[] array = new int[NUM];
        Arrays.fill(array, 0);

        for (int i = 0; i < S1.length(); i++) {
            int val = S1.charAt(i);
            array[val]++;
        }
        for (int i = 0; i < S2.length(); i++) {
            int val = S2.charAt(i);
            array[val]--;
            if (array[val] < 0) {
                return false;
            }
        }
        return true;
    }

    public boolean solutionSort(String S1, String S2) {
        char[] StringA = S1.toCharArray();
        char[] StringB = S2.toCharArray();
        Arrays.sort(StringA);
        Arrays.sort(StringB);
        String A = new String(StringA);
        String B = new String(StringB);
        return A.equals(B);
    }

    public static void main(String[] args) {
        String A = "abcde";
        String B = "abcde";
        String C = "edcba";
        String D = "hjkkl";
        String E = "jkla";

        CheckPermutation Solution = new CheckPermutation();
        System.out.println(Solution.solution(A, B));
        System.out.println(Solution.solution(A, C));
        System.out.println(Solution.solution(A, D));
        System.out.println(Solution.solution(A, E));
        System.out.println(Solution.solution(D, E));
        System.out.println(Solution.solutionSort(A, B));
        System.out.println(Solution.solutionSort(A, C));
        System.out.println(Solution.solutionSort(A, D));
        System.out.println(Solution.solutionSort(A, E));
        System.out.println(Solution.solutionSort(D, E));
    }
}