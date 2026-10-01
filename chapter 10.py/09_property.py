class Student:
    def __init__(self,phy,chem,mth):
        self.phy = phy
        self.chem = chem
        self.mth = mth

    @property
    def percantage(self):
        return str((self.phy + self.chem + self.mth) /3 ) + "%"
    
stu1 = Student(87,98,78)
print(stu1.percantage)

stu1.phy = 44
print(stu1.percantage)