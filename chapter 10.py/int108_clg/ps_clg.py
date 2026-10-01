# num1 = int(input("enter the number : "))

# print(f"squere of {num1} is {num1*num1}")


# x1=[1,2,3,5,8]

# sum = 0
# for z in x1:
#     sum = sum+z
# print(sum)

# n = 1234
# rev = 0
# while n > 0:
   
#     rev = rev * 10 + (n % 10) 
#     n //= 10
# print(rev)

# for i in range(1, 6):
#     for j in range(1, i + 1):
#       print("*", end="")
#     print()


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(i, end=" ")
#         j += 1
#     print()
#     i += 1

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return ('num is not prime')
#     return True

# print(isPrime(12))

# a = 0
# b = 1
# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b

# s = "madam"
# print("Palindrome" if s == s[::-1] else "Not Palindrome")

# for i in range(65, 70):
#     for j in range(65, i + 1):
#         print(chr(j), end=" ")
#     print()


# Railway ticket tuple storing journey details
# journey = (
#     "Passenger Name: Varun Singh",
#     "Train No: 12345",
#     "From: Delhi",
#     "To: Mumbai",
#     "Class: Sleeper",
#     "Date: 12-12-2025",
#     "From: Delhi"  # duplicate value for count() example
# )

# # 1. Using index() to find position of a detail
# from_index = journey.index("From: Delhi")
# print("Index of 'From: Delhi':", from_index)

# # 2. Using count() to count occurrences of a detail
# from_count = journey.count("From: Delhi")
# print("Count of 'From: Delhi':", from_count)

# # Display the whole tuple (optional)
# print("Full Journey Tuple:")
# for detail in journey:
#     print(detail)
# # print(journey)

# my_list = ["a", "b", "c"]
# my_str = "".join(my_list)     # Without space
# print(my_str)

# nums = ['1', '2', '3']
# str_list = [int(i) for i in nums]
# print(str_list)
# s = "1 2 3 4 5"
# int_list = [int(i) for i in s.split()]
# print(int_list)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
