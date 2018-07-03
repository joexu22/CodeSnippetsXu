import java.awt.SystemTray;
import java.util.*;

class ArrayAdding {
    public static void main(String[] arg) {
        // Understanding Hashtables
        Hashtable h = new Hashtable();
        Hashtable h1 = new Hashtable();

        // Some Training With Array Cloning
        int[] a = new int[] { 1, 2, 3, 4, 5 };
        int[] b = new int[5];

        // Quick Code Calculating The Adding Of Two Numbers
        int[] numbers = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int target = 15;
        Hashtable sums = new Hashtable();
        for (int n : numbers) {
            sums.put(n, target - n);
        }
        System.out.println(sums);
        for (int n : numbers) {
            if (sums.containsKey(n)) {
                System.out.println(n + " and " + sums.get(n) + " are a pair that adds up to " + target);
            }
        }

        h.put(3, "Joe");
        h.put(2, "Is");
        h.put(1, "Cool");

        h1 = (Hashtable) h.clone();
        h.put(4, "But");
        System.out.println("values in clone: " + h1);
        h.clear();
        System.out.println("after cleaning: " + h);
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
        b = a.clone();
        a[0] = 10;
        for (int i = 0; i < b.length; i++) {
            System.out.println(b[i]);
        }
    }
}