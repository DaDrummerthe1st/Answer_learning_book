import datetime

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
    transaction_id = 0

    def __init__(self, account_holder, balance, transactions):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = transactions
        self.transactions = {}

    def deposit(self, input_value):
        if input_value > 0 and self.account_holder != "":
            self.transactions.update(
                {self.transaction_id:
                     {self.account_holder:
                          {f'{datetime.datetime.now()}': input_value}
                      }
                 }
            )
            self.transaction_id += 1
        # print(self.transactions)
        for transaction_account in self.transactions:
            print(transaction_account)
            # for moment, dough in transaction_account:
            #    print(dough)

    def withdraw(self):
        pass


class TestRunBankaccount(BankAccount):
    def __init__(self, account_holder, balance, transactions, instance_name) -> None:
        super().__init__(account_holder, balance, transactions)
        self.instance_name = instance_name
        self.run_Bankaccount()
        self.test_deposit()

    def run_Bankaccount(self):
        self.instance_name = BankAccount(account_holder='1', balance=0, transactions={})
        print(f'BankAccount initiated as {self.instance_name}')

    def test_deposit(self):
        print('test_deposit() initiated')

        self.instance_name.deposit(input_value=15)
        for value in range(3, 36, 3):
            self.instance_name.deposit(input_value=value)


name_of_the_game = "first_try"
yesorno = TestRunBankaccount(name_of_the_game)
transaction_keys = name_of_the_game.transactions.keys()
print(name_of_the_game)
