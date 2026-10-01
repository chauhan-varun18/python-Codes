# recursion = calling itself means khud ko call krna

# 1! = 1  hota h (0 k bhi fac 1 hota h)
# 2! = 2*1  
# 3! = 3*2*1  
# 4! = 4*3*2*1  
# 5! = 5*4*3*2*1  
# to factorial(n) = n * n-1 * .....3 * 2 * 1

# factorial(n) = n * factorial (n-1)!

def factorial(n):
    if (n<=1): #(n==1 or n==0):ek hi baat h
        return n
    return n * factorial(n-1)

n = int(input("enter a num.: "))
print(f"factorial of this num. is : {factorial (n)}")
