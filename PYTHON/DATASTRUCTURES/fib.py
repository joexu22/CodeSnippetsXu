def fib(n):
    first = 0
    second = 1
    count = 2
    array = [first, second]

    while count <= n:
        next_num = first + second
        first = second
        second = next_num
        array.append(next_num)
        count += 1
    
    return array

print(fib(10))

