import java.util.*;

class IsUnique {
    public boolean mySolution(String S) {
        HashMap<Character, Boolean> characters = new HashMap<>();
        for (int i = 0; i < S.length(); i++) {
            if (characters.containsKey(S.charAt(i))) {
                return false;
            } else {
                characters.put(S.charAt(i), true);
            }
        }
        return true;
    }

    public boolean bookSolution(String S) {
        // understand the implication of strings
        // this assumes ASCII
        if (S.length() > 128) {
            return false;
        }
        boolean[] char_set = new boolean[256];
        for (int i = 0; i < S.length(); i++) {
            int val = S.charAt(i);
            if (char_set[val]) {
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }

    public void printASCIIcode(String S) {
        for (int i = 0; i < S.length(); i++) {
            int value = S.charAt(i);
            System.out.println(value);
        }
    }

    public void bitVector(String S) {
        int checker = 0;
        for (int i = 0; i < S.length(); i++) {
            int val = S.charAt(i) - 'a';
            System.out.println(1 << val);
        }
    }

    public static void main(String[] args) {
        String A = "abcdefghijk";
        String B = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        String C = "aa";
        String D = "abcdefggfedcba";
        IsUnique Solution = new IsUnique();
        System.out.println(Solution.mySolution(A));
        System.out.println(Solution.mySolution(B));
        System.out.println(Solution.bookSolution(C));
        System.out.println(Solution.bookSolution(D));
        // Solution.printASCIIcode(B);
        // Solution.bitVector(A);
    }
}