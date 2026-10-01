# n = int(input("num: "))

# a,b=0 , 1
# for i in range(n):
#     print(a, end=" ")
#     a,b = b  , a+b

# n  = int(input("rows"))
# for i in range(1,n+1):
#     print("*" * i)

# n = int(input("rows: "))
# for i in range(n , 0 , -1):
#     print("*" * i)

n = int(input("num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, "",end="")
    print()
