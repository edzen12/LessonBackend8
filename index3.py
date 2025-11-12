class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): #пополнение счёта на указанную сумму
        if amount >0:
            self.balance += amount
            return self.balance
        
    def withdraw(self, amount): #снятие денег со счёта
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Недостаточно средств")

    def info(self):
        return f"Имя: {self.owner}, У вас: {self.balance}сом"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def open_account(self, owner):
        account = BankAccount(owner)
        self.accounts.append(account)
        print(f"Счет открыт на {owner}")
        return account

    def find_account(self, owner):
        for acc in self.accounts:
            if acc.owner == owner:
                print(f"Найден {owner}")
                return acc
        print(f"Клиент {owner} не найден в банке {self.name}")

    def transfer(self, from_owner, to_owner, amount):
        from_acc =  self.find_account(from_owner)
        to_acc =  self.find_account(to_owner)
        if not from_acc or not to_acc:
            print("перевод невозможен, совпадении нет")
            return
        if amount <= 0:
            print("Сумма должна быть выше 0")
            return
        if from_acc.balance < amount:
            print("Недостаточно средств")
            return
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Перевод {amount}сом от {from_owner} к {to_owner} успешен")

bank = Bank('Mbank')
acc1 = bank.open_account('Urmat')
acc2 = bank.open_account('Danil')
acc1.deposit(5000)
acc2.deposit(3000)
bank.transfer('Urmat', 'Danil', 5000)
print(acc1.info())
print(acc2.info())