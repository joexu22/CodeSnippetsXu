public class LoopFactorial
{
    public static void main(String[] args)
    {
        final int BIG_NUMBER = 100;
        for(int i = 0; i <= BIG_NUMBER; i++)
        {
            System.out.println(i + "! is " + CalcFactorial(i));
        }
    }

    public static double CalcFactorial(int num)
    {
        double result = 1;
        for (int i = 2; i <= num; i++)
        {
            result *= i;
        }
        return result;
    }
}