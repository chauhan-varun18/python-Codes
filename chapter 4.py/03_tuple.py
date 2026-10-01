# Example tuple
mytuple = (1, 2,6, 3, 2, 4,5, 2)

# Count how many times 2 appears
print(mytuple.count(2))  # Output: 3

# Find the index of the first occurrence of 3
print(mytuple.index(6))  # Output: 2

t = (10, 20, 30)
print(t[0])   # Output: 10
print(t[-1])  # Output: 30

t = (1, 2, 3, 4, 5)
print(t[1:4])   # Output: (2, 3, 4)

a = (1, 2)
b = (3, 4)
print(a + b)   # Output: (1, 2, 3, 4)

t = (1, 2)
print(t * 3)   # Output: (1, 2, 1, 2, 1, 2)

t = (10, 20, 30)
print(20 in t)   # True
print(50 not in t)  # True

t = ("apple", "banana", "cherry")
for item in t:
    print(item)

t = (1, 2, 3, 4)
print(len(t))   # Output: 4

t = (10, 20, 30)
print(sum(t))   # Output: 60

# Packing
t = (1, "hello", 3.5)

# Unpacking
a, b, c = t
print(a)  # 1
print(b)  # hello
print(c)  # 3.5
