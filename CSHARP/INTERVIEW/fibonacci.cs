using System;

namespace InterviewExcersize{
    class IthFibonacci {
        static int Fibonacci(int n)
        {
            /* seed values */
            int x = 1;
            int y = 1;
            int z;
            
            /* base cases */
            if (n == 0) return 0;
            if (n == 1) return x;
            if (n == 2) return y;

            /* non recursive method */
            for (int i = n; i > 2; i--)
            {
                z = x + y;
                x = y;
                y = z;
            }
            return y;
        }

        static void Main(string[] args) {
            /* reads in number i*/
            Console.WriteLine("Enter Ith Number:");
            string ith = Console.ReadLine();
            int num = Int32.Parse(ith);
            Console.WriteLine("Ith Fibonacci Number:");
            Console.WriteLine(Fibonacci(num));
            Console.ReadLine();
        }
    }
}