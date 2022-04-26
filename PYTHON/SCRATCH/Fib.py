def factorial(n):
    
    def heaper(n, acc):
        if n == 0:
            return acc
        else:
            return heaper(n-1, acc*n)
    
    return heaper(n, 1)

# def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Test Cases

print(factorial(5))
print(fibonacci(6))
