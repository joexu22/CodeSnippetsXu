public class LongestPalindrome {
    static void printSubStr(String str, int low, int high) {
        System.out.println(str.substring(low, high + 1));
    }

    public int longestSubString(String str) {
        int Result = 0;
        int StringLength = str.length();
        boolean[][] table = new boolean[StringLength][StringLength];

        // tests for single character
        for (int i = 0; i < StringLength; i++) {
            table[i][i] = true;
        }

        if (StringLength > 0) {
            Result = 1;
        }

        // test for 2 characters
        int start = 0;
        for (int i = 0; i < StringLength - 1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                table[i][i + 1] = true;
            }
            start = i;
            Result = 2;
        }

        // test for 3 or greater chracters
        // k being length of the string
        for (int k = 3; k <= StringLength; k++) {
            for (int i = 0; i + k <= StringLength; i++) {
                int j = i + k - 1;
                if (table[i + 1][j - 1] && (str.charAt(i) == str.charAt(j))) {
                    table[i][j] = true;
                    if (k > Result) {
                        start = i;
                        Result = k;
                    }
                }
            }
        }

        System.out.print("Longest palindrome substring is: ");
        printSubStr(str, start, start + Result - 1);

        return Result;

    }

    public static void main(String[] args) {
        String S = "TestinggnitseT";
        LongestPalindrome Solution = new LongestPalindrome();
        System.out.println(Solution.longestSubString(S));
    }
}