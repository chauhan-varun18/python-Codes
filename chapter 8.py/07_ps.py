# c/5 = f-32/9
def f_to_c():
    return 5*(f-32)/9

f = int(input("enter a temp.: "))
print (f"{round (f_to_c(),2)} Degree C")