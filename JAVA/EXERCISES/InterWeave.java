import java.util.*;

public class InterWeave {
    public static int[] interweave(int[] a, int[] b) {
        int[] out = new int[a.length + b.length];
        int j = 0;

        int maxLength = Math.max(a.length, b.length);
        for (int i = 0; i < maxLength; i++) {
            if (i < a.length) {
                out[j++] = a[i];
            }
            if (i < b.length) {
                out[j++] = b[i];
            }
        }
        return out;
    }

    public static void main(String[] args) {
        int[] test1 = new int[] { 1, 2, 3, 4, 5 };
        int[] test2 = new int[] { 5, 4, 3, 2, 1 };
        int[] test3 = interweave(test1, test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
        System.out.println(Arrays.toString(interweave(test1, test2)));
        System.out.println(Arrays.toString(test3));
    }
}