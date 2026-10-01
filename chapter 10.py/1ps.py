class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi", self.name, "your score is",sum/3)

s1 = Student("varun",[53,55,85])
s1.get_avg()

s1 = Student("xyz",[23,5,45])
s1.get_avg()
