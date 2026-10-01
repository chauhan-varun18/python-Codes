# str = "varunthakur"
# print(str[:5])

# str = "apple"
# print(str[-3:])

str = "i am varun thakur from up"
str = str.capitalize()
print(str) #string ko capital ltr se start kr dega

str = "i am varun thakur from up"
print (str.endswith("up"))
print (str.endswith("from "))

str = "i am varun thakur from up"

print(str.replace("up", "uttar pradesh"))

print(str.find("from"))

print(str.count("a"))


m = int(input())
if (m>=90):
    print("a")

elif(m>=80):
    print("b")

else:
    print("d")    