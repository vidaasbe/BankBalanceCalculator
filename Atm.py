class Atm(object):
    def __init__(self,name,atmnumber,currentbalance):
        self.name = name
        self.currentbalance = currentbalance
        self.atmnumber = atmnumber

    def balanceInquiry(self):
        print("Your Balance is: ", self.currentbalance)
    
    def cashWithdraw(self,amount):
        self.currentbalance = self.currentbalance - amount
        print("Your Balance After Widthrawal is: ", self.currentbalance)
    
    def deposit(self,amount):
        self.currentbalance = self.currentbalance + amount
        print("Your Balance After Depositing is: ", self.currentbalance)
    
vida = Atm("vida",28379,5000)

vida.balanceInquiry()
vida.cashWithdraw(300)
vida.deposit(500)