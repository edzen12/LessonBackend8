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
        self._cargo_list = []
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
class Truck(Vehicle):
    def __init__(self, model, capacity_kg, base_fee, axles):
        super().__init__(model, capacity_kg, base_fee)
        self._axles = axles

    def info(self):
        return f"Грузовик {self._model}, осей: {self._axles}, вес {self.total_weight}, цена {self.total_cost()}"

class Van(Vehicle):
    def __init__(self, model, capacity_kg, base_fee, volume_m3):
        super().__init__(model, capacity_kg, base_fee)
        self._volume_m3 = volume_m3

    def info(self):
        return f"Грузовик {self._model}, объем: {self._volume_m3} м3, вес {self.total_weight}, цена {self.total_cost()}"   

class BikeCourier(Vehicle):
    def __init__(self, model, capacity_kg, base_fee, speed):
        super().__init__(model, capacity_kg, base_fee)
        self._speed = speed

    def info(self):
        return f"«Курьер {self._model}, скорость: {self._speed} км/ч, вес {self.total_weight}, цена {self.total_cost()}"   
    

# Класс Fleet (автопарк):
# защищённый список _vehicles
# метод add_vehicles(*vehicles): добавляет любое количество транспортов
# метод find_vehicles(**filters): поиск по model, axles, speed, capacity и т.п.
# метод all_vehicles()

# Класс TransportCompany:
# атрибут name
# объект fleet
# приватный атрибут __income + свойство income
# метод send_vehicle(model):
# находит транспорт по модели
# добавляет total_cost() к доходу
# удаляет транспорт из автопарка
# метод status(): доход и количество оставшихся транспортов
# метод list_vehicles(): список транспорта через info()