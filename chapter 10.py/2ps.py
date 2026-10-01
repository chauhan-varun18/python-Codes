class Amount:
    def __init__(self,account_no,balance):
        self.acc = account_no
        self.bal = balance

    def debit(self,ammount):
        self.bal -= ammount
        print("Rs. ", ammount,"was debited")
        print("you balance is",self.bal)

    def credit(self,ammount):
        self.bal += ammount
        print("Rs. ", ammount,"was credited")
        print("you balance is",self.bal)

    def get_total_bal(self):
        return self.bal

acs = Amount(4352 , 1000)
acs.debit(500)
print("\n")
acs.credit(800)
