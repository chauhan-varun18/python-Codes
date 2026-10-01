class Car:
    color = "Black"

    @staticmethod
    def start():
        print("car started") 

    @staticmethod
    def stop():
        print("car stopped") 

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Supra(ToyotaCar):
    def __init__(self,type,brand):
        
        super().__init__(brand)
        self.type = type

c1 = Supra("diesel","Toyota")
print(c1.type)
print("\n")

print(c1.brand)
print(c1.start())