class BankAccounts(object):
    def __init__(self,name,accounttype,accountnumber,currentbalance):
        self.name = name
        self.currentbalance = currentbalance
        self.accounttype = accounttype
        self.accountnumber = accountnumber

    def balanceInquiry(self):
        print("Your Balance is: ", self.currentbalance)
    
    def withdraw(self,amount):
        self.currentbalance = self.currentbalance - amount
        print("Your Balance After Widthrawal is: ", self.currentbalance)
    
    def deposit(self,amount):
        self.currentbalance = self.currentbalance + amount
        print("Your Balance After Depositing is: ", self.currentbalance)
    
vida = BankAccounts("vida","savings",28379,5000)

vida.balanceInquiry()
vida.withdraw(300)
vida.deposit(500)