class Car:
    def __init__(self):
        self.clutch = False
        self.brk  = False
        self.acc = False
        print("car not started")
            # yha (abstruction m) par jo kaam ki cheej h bahi deta h baaki ki unnecessary cheeze print na hoti
    def start(self):
        self.clutch = True
        self.brk  = False
        self.acc = True 
        print("car started")


c1 = Car()
c1.start()
