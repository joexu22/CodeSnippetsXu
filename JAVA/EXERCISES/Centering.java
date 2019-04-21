class Centering {
    // two indexes
    // a - tracks how many numbers are smallers does swap
    // b - goes and scans whole array

    public static int[] partition(int[] arr, int low, int high) {
        int pv = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pv) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return arr;
    }

    public static void main(String[] args) {
        int[] test = new int[] { 2, 6, 5, 4, 3, 1 };
        partition(test, 0, test.length - 1);
        for (int i : test) {
            System.out.print(i + " ");
        }
    }
}