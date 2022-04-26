mathematical_significant_list_definitions = """
1, the multiplicative identity. Also the only natural number (not including 0) that isn't prime or composite.
2, the base of the binary number system, used in almost all modern computers and information systems.
3, 22-1, the first Mersenne prime. It is the first odd prime, and it is also the 2 bit integer maximum value.
4, the first composite number
6, the first of the series of perfect numbers, whose proper factors sum to the number itself.
9, the first odd number that is composite
11, the fifth prime and first palindromic multi-digit number in base 10.
12, the first sublime number.
17, the sum of the first 4 prime numbers, and the only prime which is the sum of 4 consecutive primes.
24, all Dirichlet characters mod n are real if and only if n is a divisor of 24.
25, the first centered square number besides 1 that is also a square number.
27, the cube of 3, the value of 33.
28, the second perfect number.
30, the smallest sphenic number.
32, the smallest nontrivial fifth power.
36, the smallest number which is perfect power but not prime power.
72, the smallest Achilles number.
255, 28 − 1, the smallest perfect totient number that is neither a power of three nor thrice a prime; it is also the largest number that can be represented using an 8-bit unsigned integer
341, the smallest base 2 Fermat pseudoprime.
496, the third perfect number.
1729, the Hardy–Ramanujan number, also known as the second taxicab number; that is, the smallest positive integer that can be written as the sum of two positive cubes in two different ways.[1]
8128, the fourth perfect number.
142857, the smallest base 10 cyclic number.
9814072356, the largest perfect power that contains no repeated digits in base ten.
"""

mathematical_significant_list = [1, 2, 3, 4, 6, 9, 11, 12, 17, 24, 25, 27, 28, 30, 32, 36, 72, 255, 341, 496, 1729, 8128, 142857, 9814072356]

filtered_list_evens = filter(lambda x: x % 2 == 0, mathematical_significant_list)

for i in filtered_list_evens:
    print(i)

filtered_list_map_2x = map(lambda x: x * 2, mathematical_significant_list)

for i in filtered_list_map_2x:
    print(i)

filtered_definitions_list = map(lambda x: x.split(), mathematical_significant_list_definitions)

for i in filtered_definitions_list:
    print(i)

