# n = 5
# fact= 1
# for i in range (1 , n+1):
#     fact *= i
#     print(fact)

# n = 1

# print(n//10)

# a = input("")
# # k = [i for i in a.split(',')]
# k = [int(i) for i in a.split(',')]

# n = 0
# for f in k:
   
#     print ((n*2),f)
#     n+=1



a = input("")
k = [int(i) for i in a.split(',')]

e = 0
o = 0

for i in k:
    if i%2 == 0:
        e+=1

    else:
        o+=1
print('even',e)
print('odd',o)

# Runner.prototype.gameOver = function() {}