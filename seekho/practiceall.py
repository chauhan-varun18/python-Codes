# my_dict = {"a": 100, "b": 200, "c": 300}

# total = sum(my_dict.values())

# print("Sum =", total)

# l1 = ['a','b','c']
# l2 = [1,2,3]

# d = dict(zip(l1,l2))
# print(d)


# my_dict = {"a": 100, "b": 200, "c": 300}
# sum = 0
# for i,j in my_dict.items():
#     sum += j

# print(sum)

# def feb (n):
#     if n ==1 or n==2:
#         return 1
    
#     else:
#         return feb(n-1) + feb(n-2)
    
# n = int(input())
# print(feb(n))

# n = 7
# a, b = 0, 1

# for i in range(n - 1):
#     a, b = b, a + b

# print("7th Fibonacci =", a)


import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

for i in range(120):
    t.penup()
    t.goto(0, 40)
    
   
    angle = i * (math.pi * 2) / 120
    
 
    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
    
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)
    
    
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()