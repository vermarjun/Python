class Account():
    def __init__(self,owner,balance) -> None:
        self.owner = owner
        self.balance = balance
    def __str__(self) -> str:
        return f'Account Owner = {self.owner} \n' f'Account Balance = {self.balance}'
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'Deposit Accepted, current balance is {self.balance}')
    def withdraw(self,amount):
        if amount > self.balance:
            print('Funds Unavailable')
        else:
            self.balance = self.balance - amount
            print(f'Cash Withdrawed, current balance is {self.balance}') 

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)