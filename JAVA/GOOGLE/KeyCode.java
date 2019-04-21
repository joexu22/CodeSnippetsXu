import java.util.*;

// My First Instinct Was All Wrong...
class KeyCode {
    public String solution(String S, int K) {
        int Kcount = 0;
        StringBuilder sb = new StringBuilder();

        char[] Schar = S.toCharArray();
        int Slength = Schar.length;

        for (int i = Slength - 1; i >= 0; i--) {
            if (Kcount == K) {
                sb.append('-');
                Kcount = 0;
            }
            if (Schar[i] != '-') {
                sb.append(Character.toUpperCase(Schar[i]));
                Kcount++;
            }
        }
        sb = sb.reverse();
        return sb.toString();
    }

    public static void main(String[] args) {
        // String S = "2-4A0r7-4k";
        String S = "r";
        String X1 = "24A0-R74K";
        String X2 = "24-A0R-74K";

        int K = 1;

        int k = 0; // tracks for the dash
        StringBuilder sb = new StringBuilder();
        char[] Schar = S.toCharArray();
        int length = S.length();
        System.out.println(length);
        for (int i = length - 1; i >= 0; i--) {
            if (k == K) {
                sb.append('-');
                k = 0;
            }
            if (Schar[i] != '-') {
                sb.append(Character.toUpperCase(Schar[i]));
                k++;
            }
        }

        System.out.println(X1);
        sb = sb.reverse();
        String S2 = sb.toString();
        System.out.println(S);
        System.out.println(S2);
    }
}