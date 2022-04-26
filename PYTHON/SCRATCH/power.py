def power(n):
    
    def healper(n, acc):
        if n == 0:
            return acc
        else:
            return healper(n-1, acc*n)
    
    return healper(n, 1)

#Test Cases
print(power(5))