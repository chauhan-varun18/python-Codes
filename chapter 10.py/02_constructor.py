class Student:
    def __init__(self,name):   #self(argument(constructer k ander dena hota h)) ki jagha or kuhuc bhi likh skte h 
        self.name = name
        print("I'm Thakur G")

S1 = Student("Varun Cahauhan")     # 1obj.
print(S1.name)


S2 = Student("Utkarsh Cahauhan")  #constrecter har ek naye obj. k sth call hota h
print(S2.name)


class Student:
    def __init__(self,name,marks):   #self(argument(constructer k ander dena hota h)) ki jagha or kuhuc bhi likh skte h 
        self.name = name
        self.marks = marks
        print("XYZ")

S1 = Student("Varun Cahauhan",97)     # 1st obj.
print(S1.name, S1.marks)


S2 = Student("Utkarsh Cahauhan",77)  #constrecter har ek naye obj. k sth call hota h
print(S2.name, S2.marks)  


class Student:
    clg_name = "LPU"
    def __init__(self,name,marks):   #self(argument(constructer k ander dena hota h)) ki jagha or kuhuc bhi likh skte h 
        self.name = name
        self.marks = marks
        print("XYZ")

S1 = Student("Varun Cahauhan",97)     # 1st obj.
print(S1.name, S1.marks, "\n")


S2 = Student("Utkarsh Cahauhan",77)  #constrecter har ek naye obj. k sth call hota h
print(S2.name, S2.marks, "\n")

# del s2.name se delete kr skte h object ko

print(S2.clg_name)  