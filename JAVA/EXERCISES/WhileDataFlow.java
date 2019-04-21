public class WhileDataFlow {
    public static void debug(String t, int s, int e, int p) {
        System.out.print(t + "[S:" + s + "-P:" + p + "-E:" + e + "]");
    }

    public static void main(String[] args) {
        int start = 0;
        int end = 10;
        int pivot = 5;
        while (start <= end) {
            debug("A:", start, end, pivot);
            while (start < pivot) {
                debug("B:", start, end, pivot);
                ++start;
            }
            while (pivot < end) {
                debug("C:", start, end, pivot);
                --end;
            }
        }
    }
}