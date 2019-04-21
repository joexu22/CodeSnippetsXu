public class RunnableTest {
    public static void main(String[] args) {
        System.out.println("=== RunnableTest ===");
        Runnable r1 = new Runnable() {

            @Override
            public void run() {
                System.out.println("Hello Run One!");
            }
        };
        Runnable r2 = () -> System.out.println("Hello World Two!");
        r1.run();
        r2.run();
    }
}