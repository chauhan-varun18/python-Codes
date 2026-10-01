def fibonacci(n):
    # base case
    if n <= 1:
        return n
    # recursive case
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a num. : "))
for i in range(n):
    print(fibonacci(i),end="")