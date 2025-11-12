# ООП - объектно-ориентированное программирование
# Наследование 
# Инкапсуляция
#     public  - публичный
#     _protected - защищенный
#     __private - приватный
# Полиморфизм

class Animal: # родительский класс
    def __init__(self, name, age, color): # контструктор класса
        self.name = name # атрибут класса
        self.__age = age  # инкапсулированный атрибут
        self.color = color  
    
    @property # декоратор
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >0 and new_age < 20:
            self.__age = new_age
    
    def info(self):
        print(f"Имя: {self.name} Возраст: {self.__age} цвет:{self.color}")

class Cat(Animal): # дочерний класс
    def mau(self):
        print("мяу-мяу")

class Dog(Animal): # дочерний класс
    def gav(self):
        print("гав-гав")




# 1) Создай класс Book, который описывает книгу.
# атрибуты:
    # title — название книги
    # author — автор
    # year — год издания
    # is_available — доступна ли книга в библиотеке (по умолчанию True)
# создать метод info() — выводит информацию о книге в виде:
# Например: "Название: <title>, Автор: <author>, Год: <year>, в наличии "
# создать метод borrow() — если книга доступна, делает is_available = False
# создать метод return_book() — делает is_available = True
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    
    def info(self):
        print(f"""Название: {self.title}, Автор: {self.author} 
              Год: {self.year} 
              в наличии {'есть' if self.is_available == True else 'нету'}""")
    def borrow(self):
        if self.is_available:
            self.is_available = False
    def return_book(self):
        if self.is_available == False:
            self.is_available = True
# создайте метод который изменяет название книги и автора

b = Book('Война и мир', "Лев Толстой", 1869)# экземпляр
c = Book('Преступление и наказание', "Фёдор Достое́вский", 1869)# экземпляр
b.borrow()
b.info()
b.return_book()
b.info()