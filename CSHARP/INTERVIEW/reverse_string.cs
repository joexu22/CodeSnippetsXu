using System;

namespace InterviewExcersize{
    class StringReverser {
        static void Main(string[] args) {
            /* reads in string */
            Console.WriteLine("Enter String:");
            string word = Console.ReadLine();
            
            /* reverses string using arrays */
            char[] array = word.ToCharArray();
            Array.Reverse(array);

            Console.WriteLine("Reversed String:");
            Console.WriteLine(array);
            Console.ReadLine();
        }
    }
}