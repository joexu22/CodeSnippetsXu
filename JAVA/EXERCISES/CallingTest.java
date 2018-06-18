public class CallingTest
{
    public static void main(String[] args)
    {
        functionOne();
        functionTwo();
        functionThree();
    }
    
    public static void functionOne() {
        System.out.println("One!");
    }

    public static void functionTwo() {
        functionOne();
        functionOne();
    }

    public static void functionThree() {
        functionOne();
        functionOne();
        functionOne();
    }
}