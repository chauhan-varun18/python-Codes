marks = {
    "varun" : 100,
    "aryan" : 38,
    "utkarsh" : 59,
    0 : "ansh"
}

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"varun" : 99 , "abhi" : 55})
print(marks)

# print(marks.get("akash")) # none dega
# print(marks["akash"]) #error dega

# marks.pop("varun")          # removes key and returns value
# marks.popitem()           # removes last inserted pair
del marks["utkarsh"]         # delete by key
# marks.clear()   # remove all items
print(marks)           