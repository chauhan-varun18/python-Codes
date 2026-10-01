class Car:
    color = "Black"

    @staticmethod
    def start():
        print("car started") 

    @staticmethod
    def stop():
        print("car stopped") 

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

c1 = ToyotaCar("fortuner")
print(c1.name)
print("\n")

c2 = ToyotaCar("supra")
print(c2.name)

print(c1.start())
print(c1.color)