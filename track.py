class Cargo:
    def __init__(self, name, weight_kg, price_per_kg):
        self._name = name
        self._weight_kg = float(weight_kg)
        self.__price_per_kg = None
        self.price_per_kg = price_per_kg 
    
    @property
    def price_per_kg(self):
        return self.__price_per_kg

    @price_per_kg.setter
    def price_per_kg(self, value):
        if value >= 5:
            self.__price_per_kg = value
            
    def cost(self): #стоимость всего груза
        return round(self._weight_kg * self.__price_per_kg, 2)

    def info(self):
        return f"{self._name}: {self._weight_kg}кг, {self.__price_per_kg}сом/кг"

class Vehicle:
    def __init__(self, model, capacity_kg, base_fee):
        self._model = model
        self._capacity_kg = capacity_kg
        self._cargo_list = [] # грузы внутри транспорта
        self.__base_fee = None 
        self.base_fee = base_fee 
    
    @property
    def base_fee(self):
        return self.__base_fee
    
    @base_fee.setter
    def base_fee(self, value):
        if value >= 100:
            self.__base_fee = value
        else:
            print("Базовая оплата должны быть от 100 и выше")

    def add_cargo(self, cargo):
        #если хватает грузоподъёмности
        if self.total_weight() + cargo._weight_kg > self._capacity_kg: 
            return False
        self._cargo_list.append(cargo) #добавляет груз
        return True

    def total_weight(self): # общий вес груза
        return sum(c._weight_kg for c in self._cargo_list)
    
    #стоимость перевозки = base_fee + суммы cost() всех грузов
    def total_cost(self): 
        total = self.__base_fee
        for c in self._cargo_list:
            total += c.cost()
        return round(total, 2)
    
    def info(self):
        return f"{self._model}, вес: {self.total_weight()}, цена: {self.total_cost()}"

# Наследники Vehicle:
class Truck(Vehicle): #грузовик
    def __init__(self, model, capacity_kg, base_fee, axles):
        super().__init__(model, capacity_kg, base_fee)
        self._axles = axles

    def info(self):
        return f"Грузовик {self._model}, осей: {self._axles}, вес {self.total_weight()}, цена {self.total_cost()}"

class Van(Vehicle): #фургон
    def __init__(self, model, capacity_kg, base_fee, volume_m3):
        super().__init__(model, capacity_kg, base_fee)
        self._volume_m3 = volume_m3

    def info(self):
        return f"Грузовик {self._model}, объем: {self._volume_m3} м3, вес {self.total_weight()}, цена {self.total_cost()}"   

class BikeCourier(Vehicle): #мото
    def __init__(self, model, capacity_kg, base_fee, speed):
        super().__init__(model, capacity_kg, base_fee)
        self._speed = speed

    def info(self):
        return f"«Курьер {self._model}, скорость: {self._speed} км/ч, вес {self.total_weight()}, цена {self.total_cost()}"   
    

class Fleet: #автопарк
    def __init__(self):
        self._vehicles = []
    
    def add_vehicles(self, *vehicles): #добавляет любое количество транспортов
        for veh in vehicles:
            self._vehicles.append(veh)

    def find_vehicles(self, **filters): #поиск по атрибутам
        res = self._vehicles
        for attr, val in filters.items():
            res = [v for v in res if hasattr(v, f"{attr}") and getattr(v, f"_{attr}") == val]
        return res 
    
    def all_vehicles(self):
        return self._vehicles

class TransportCompany:
    def __init__(self, name):
        self.name = name 
        self.fleet = Fleet()
        self.__income = 0

    @property
    def income(self):
        return self.__income
     
    def send_vehicle(self, model): #находит транспорт по модели
        for v in self.fleet._vehicles:
            if v._model == model:
                self.__income += v.total_cost()
                self.fleet._vehicles.remove(v)
                return True
        return False

    def status(self):
        return f"Доход: {self.__income}, Транспорта осталось: {len(self.fleet._vehicles)}"

    def list_vehicles(self): 
        return [v.info() for v in self.fleet._vehicles]
    


c1 = Cargo("Сталь", 500, 10)
c2 = Cargo("Дерево", 200, 7)
c3 = Cargo("Хрупкий груз", 50, 20)
c4 = Cargo("Письма", 5, 5)
 
t1 = Truck("Volvo FH", 2000, 1500, axles=4) # Создаем транспорт
t2 = Truck("MAN TGX", 1800, 1400, axles=3)
v1 = Van("Mercedes Sprinter", 1200, 800, volume_m3=15)
v2 = Van("Ford Transit", 1000, 700, volume_m3=12)
b1 = BikeCourier("Honda Courier", 50, 150, speed=90)
b2 = BikeCourier("Yamaha Fast", 40, 120, speed=85)


t1.add_cargo(c1)
t1.add_cargo(c2)
v1.add_cargo(c3)
b1.add_cargo(c4)
company = TransportCompany("MegaTrans Logistics")
company.fleet.add_vehicles(t1, t2, v1, v2, b1, b2) #Добавляем транспорт в автопарк

print("Все ТС:")
for info in company.list_vehicles():
    print(info)

print("\nПоиск грузовиков с 4 осями:")
for v in company.fleet.find_vehicles(axles=4):
    print(v.info())

print("\nПоиск фургонов объемом 15 м³:")
for v in company.fleet.find_vehicles(volume_m3=15):
    print(v.info())

print("\nПоиск курьера со скоростью 90 км/ч:")
for v in company.fleet.find_vehicles(speed=90):
    print(v.info())
 
company.send_vehicle("Volvo FH")
print(company.status()) 

print("\nОставшиеся ТС:")
for info in company.list_vehicles():
    print(info)