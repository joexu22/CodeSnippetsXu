import java.util.*;

class StringBuilderTest {
    public static void main(String[] args) {
        // time measurement using StringBuilder
        long NANOSECOND_IN_MILLISECOND = 1000000;
        int ONE_MILLION = 1000000;
        long startTime = System.nanoTime();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ONE_MILLION; i++) {
            sb.append(i);
        }
        String test = sb.toString();
        System.out.println("StringBuilder Test ------------------------------------");
        System.out.println("Time elapsed: " + (System.nanoTime() - startTime) / NANOSECOND_IN_MILLISECOND + " milliseconds");
        
        // time measurement using String Concatenation
        startTime = System.nanoTime();
        String test2 = "";
        //ONE_MILLION is too much for my computer
        for (int i = 0; i < ONE_MILLION; i++) {
            test2 += i;
        }   
        System.out.println("StringBuilder Test ------------------------------------");
        System.out.println("Time elapsed: " + (System.nanoTime() - startTime) / NANOSECOND_IN_MILLISECOND + " milliseconds");
    }
}