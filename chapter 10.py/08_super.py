class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started") 

    @staticmethod
    def stop():
        print("car stopped") 

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

c1 = ToyotaCar("fortuner","petrol")
print(c1.name)
print(c1.type)

