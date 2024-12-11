# 6
print('\n')
print("""
6.
a) Skapa en klass som heter BankAccount.

Klassen skall ha attributet account_holder som visar 
kontoinnehavarens namn samt attributet balance som visar
kontoinnehavarens balans.

Klassen skall ha metoden deposit() för att kunna sätta in pengar
på kontot samt metoden withdraw() för att kunna ta ut pengar
från kontot.

Om bankinnehavaren försöker ta ut mer pengar än
vad som finns på kontot skall meddelandet “Balance too low”
printas ut.

b) Skapa en instans av klassen och testa så klassen funkar så som
du förväntar dig. Du kan till exempel prova printa ut attributen,
sätta in pengar och ta ut pengar.
""")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print(f'can\'t withdraw. Balance {self.balance} is less than withdrawal {amount}, balance is too low!')

    def print_balance(self):
        print(f'Balance: {self.balance}')

account1 = BankAccount(account_holder='Joakim', balance=0)

account1.print_balance()
account1.deposit(100)

account1.print_balance()
account1.withdraw(50)
account1.print_balance()
