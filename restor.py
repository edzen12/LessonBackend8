class Ingredient:
    def __init__(self, name:str, quantity_grams:float, price_per_gram):
        self._name = name 
        self._quantity = float(quantity_grams) 
        self.__price_per_gram = None 
        self.price_per_gram = price_per_gram 

    @property
    def price_per_gram(self):
        return self.__price_per_gram
    
    @price_per_gram.setter
    def price_per_gram(self, value):
        if value>=0.1:
            self.__price_per_gram = float(value)
    
     
    def cost(self, weight_grams): #возвращает стоимость weight граммов
        return float(weight_grams)*self.__price_per_gram
    

class Dish:
    def __init__(self, name, ingredients, base_price):
        self._name = name 
        self._ingredients = dict(ingredients) 
        self.__base_price = None 
        self.base_price = base_price
    
    @property
    def base_price(self):
        return self.__base_price
    
    @base_price.setter
    def base_price(self, value):
        if value>20:
            self.__base_price = float(value) 
    
    def total_cost(self): #стоимость ингредиентов + base_price
        pass
    
    def info(self): #будет переопределён в наследниках
        pass

class HotDish(Dish): #горячее блюдо
    def __init__(self, name, ingredients, base_price, spicy_level):
        super().__init__(name, ingredients, base_price)
        self._spicy_level = spicy_level #(0–5)
# Доп. атрибут: _spicy_level (0–5)
# info(): «Горячее блюдо: <name>, острота <spicy>, цена <total_cost>»
# • Dessert — десерт
# Доп. атрибут: _sweetness (0–10)
# info(): «Десерт: <name>, сладость <sweetness>, цена <total_cost>»
# • Drink — напиток
# Доп. атрибут: _volume_ml
# info(): «Напиток: <name>, объем <volume> мл, цена <total_cost>»

# Класс Kitchen:
# защищённый список _dishes
# метод add_dishes(*dishes): принимает любое количество блюд
# метод find_dishes(**filters): поиск по любым параметрам (name, spicy_level, sweetness и т.д.)
# метод remove_dish(dish)
# метод all_dishes(): возврат копии списка

# Класс Restaurant:
# атрибут name
# объект kitchen
# приватный атрибут __income (через свойство только чтение)
# метод order_dish(dish_name): продаёт блюдо, увеличивает доход, убирает из меню
# метод menu(): список всех блюд через info()
# метод status(): доход и количество оставшихся блюд 