student = {
    "name" : "varun",
    "sub" : {   #dict k ander dict bnane ko nasted dict khete h
        "phy" :94,
        "chem" :96,
        "maths" :93
    }
}

print(student)

print(student["sub"]["chem"])

print(student.keys())  # ya values kra lo

# print(student["name3"]) # ye error dega jisse aage k code nhi chlega

print(student.get("name3"))  # ye none dega jisse aage k code chl skta h

student.update({"city" : "spn" , "age" : 17})
print(student)