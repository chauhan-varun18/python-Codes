# 5! = 1 * 2 * 3 * 4 * 5

n = int(input('enter a number:'))
product = 1
for i in range(1,n+1): # n+1 isliye quki range n-1 tk jaati h but hume n tk jana h isiliye n+1lgya jisse n tk jaye
    product = product*i

print(f" {n} {product}")


