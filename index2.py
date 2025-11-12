class Car: # создание класса
    def __init__(self, brand, model): # конструктор класса
        self.brand = brand # атрибут класса
        self.model = model # атрибут класса
        self.speed = 0 # атрибут класса
        self.is_going = False # состояние (едет\не едет)
    
    def start(self, new_speed):
        self.speed += new_speed
        self.is_going = True 

    def stop(self):
        self.speed = 0
        self.is_going = False
    
    def rename(self, new_brand, new_model):
        self.brand = new_brand
        self.model = new_model

    def info(self): # метод класса - функция внутри класса
        return f"{self.brand} {self.model} скорость:{self.speed} Машина:{'едет' if self.is_going else 'не едет'}"

katya = Car('kia', 'k5')
katya.start(50)
print(katya.info())
katya.stop()
katya.rename('BMW', 'x5')
print(katya.info())