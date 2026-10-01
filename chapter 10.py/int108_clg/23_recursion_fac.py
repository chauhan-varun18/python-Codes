def fact(n):
    if (n == 0 or n == 1):
        return (1)
    
    return n * fact(n - 1)

print(fact(6))



def calc_sum(n):
    if( n == 0):
        return 0
    
    return (calc_sum(n-1) + n)

print(calc_sum(10))