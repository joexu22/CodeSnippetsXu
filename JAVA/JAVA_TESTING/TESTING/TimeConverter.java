import java.util.*;

class TimeConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println("Please Enter Day(s): ");
        // int days = sc.nextInt();
        // sc.close();
        int days = 1;
        int hours = 24 * days;
        int minutes = 60 * hours;
        int seconds = 60 * minutes;
        
        System.out.format("%d hours / %d minutes / %d seconds", hours, minutes,
        seconds);
    }
}