a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("HCF =", a)
print("\n")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if(a==0 or b==0):
    print("not HCF")

while(a%b!=0):
    x=a%b
    a=b
    b=x
print("HCF" ,b)