import java.util.*;

class InsertionSort {
    // Some Basic Intuition On Insertion Sort...
    public int[] sort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int j = i; // the new element is shuffled in and inserted
            while (j > 0 && arr[j] < arr[j - 1]) {
                int temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
                j--;
            }
        }
        return arr;
    }

    public void printArrayStuff(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public void printArrayStuff(char[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public boolean checkSortedIncreasing(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public char[] changeToChar(int[] arr) {
        char[] result = new char[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = (char) arr[i];
        }
        return result;
    }

    public static void main(String[] args) {
        String A = "INSERTIONSORT";
        int[] testArray = new int[A.length()];
        for (int i = 0; i < A.length(); i++) {
            int val = (int) A.charAt(i);
            testArray[i] = val;
        }

        int[] testArray2 = testArray.clone();

        InsertionSort Solution = new InsertionSort();
        Solution.printArrayStuff(A.toCharArray());
        Solution.printArrayStuff(testArray);
        Solution.printArrayStuff(Solution.sort(testArray));
        Solution.printArrayStuff(Solution.changeToChar(testArray));


        System.out.println(Solution.checkSortedIncreasing(testArray2));
        System.out.println(Solution.checkSortedIncreasing(Solution.sort(testArray2)));
    }
}
