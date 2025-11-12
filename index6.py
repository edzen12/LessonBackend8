class Computer:
    def __init__(self, id, hourly_rate):
        self.__id = id 
        self.__hourly_rate = hourly_rate # цена за час
        self._is_busy = False # True-занят/False-свободен
        self._current_client = None
        self._hours = 0

    @property
    def id(self):
        return self.__id
    
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, newPrice):
        if newPrice >= 50 and newPrice <= 500:
            self.__hourly_rate = newPrice

    def start_session(self, client, hours):
        if self._is_busy:
            print("Комп занят")
            return False
        total_cost = self.__hourly_rate * hours 
        if not client.pay(total_cost):
            print(f"{client.name} не смог оплатить")
            return False
        
        self._is_busy = True
        self._current_client = client
        self._hours = hours
        print(f"""{client.name} сел за комп {self.__id} 
              на {hours}ч, оплачено {total_cost}сом""")
        return True

            
    def end_session(self):
        self._is_busy = False
        self._current_client = None 
        self._hours = 0
        print(f"Комп {self.__id} освободился")

    def info(self):
        status = 'Занят' if self._is_busy else 'Свободен'
        client_name = self._current_client.name if self._current_client else '-'
        return f"комп {self.__id}: {status}, клиент: {client_name}"


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount): # уменьшает баланс, если хватает денег.
        if self.balance>= amount:
            self.balance -= amount
            return True
        return False

    def add_balance(self, amount): # пополнение счёта.
        if amount >0:
            self.balance += amount

    def info(self):
        return f"Имя: {self.name}, Баланс: {self.balance}сом"

class Club:
    def __init__(self,name):
        self.name = name 
        self.computers = []
        self._income = 0 # доход
        
    def add_computer(self, computer):
        self.computers.append(computer)

    def find_free_computer(self):
        for comp in self.computers:
            if not comp._is_busy:
                return comp
        return None 

    def serve_client(self, client, hours): # садим чела на свободный комп
        comp = self.find_free_computer()
        if not comp:
            print("Нет свободных компов")
            return 
        if comp.start_session(client, hours):
            self._income += comp.hourly_rate*hours

    def end_all_sessions(self):
        for comp in self.computers:
            comp.end_session()

    def show_status(self):
        print(f"Комп клуб {self.name}")
        for comp in self.computers:
            print(comp.info())
        print(f'Выручка: {self._income}сом\n')

club = Club('PythonClub')
club.add_computer(Computer(1, 100))        
club.add_computer(Computer(2, 80)) 

client1=Client('Урмат', 500)
client2=Client('Асинат', 600)
club.serve_client(client1, 2) #клиент,сколько часов
club.serve_client(client2, 3)
club.show_status()
club.end_all_sessions()
club.show_status()