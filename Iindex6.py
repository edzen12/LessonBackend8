# Наследование
# Инкапсуляция-сокрытие данных
#     public 
#     _protected - защищенная
#     __private - приватная 

# сделайте атрибут age приватным
class Cat:
    def __init__(self, name, age): 
        self.name = name # атрибут
        self.__age = age # атрибут
    
    #декораторы
    @property #getter # setter #deleter
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, newAge):
        if newAge>0 and newAge<20:
            self.__age = newAge
            return self.__age

ca = Cat('felix', 4) # экземпляр
ca.age = 19
print(ca.age)

