class BaseBook:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 100:
            self.__price = value 

    def info(self):
        return f"{self._title} {self._author} {self.price}"

class Book(BaseBook):
    def info(self):
        return f"Книга:{self._title} автор: {self._author} {self.price}сом" 

class EBook(BaseBook): 
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb
    
    def info(self):
        return f"Электронная книга:{self._title} автор: {self._author} {self.price}сом, файл {self._file_size_mb}МБ»" 

class AudioBook(BaseBook): 
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min
    
    def info(self):
        return f"Электронная книга:{self._title} автор: {self._author} {self.price}сом, длительность {self._duration_min}мин»"  

class Inventory:
    def __init__(self):
        self._books = []

    def add_books(self, *books): #принимает любое количество объектов книг
        for i in books:
            self._books.append(i)

    def find_books(self, **filters): 
        res = self._books
        for key, value in filters.items():
            res = [b for b in res if getattr(b, f"_{key}", None)==value]
        return res 

    def remove_book(self, book): 
        if book in self._books:
            self._books.remove(book)
    
    def all_books(self):
        return self._books.copy()
 

class BookStore:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.__income = 0
    
    @property
    def income(self):
        return self.__income
    
    def sell_book(self, title): #ищет по названию, удаляет книгу, увеличивает доход
        for book in self.inventory.all_books():
            if book._title == title:
                self.__income += book.price
                self.inventory.remove_book(book)
                return True
        return False

    def show_status(self): 
        return {
            'Магазин':self.name,
            'Доход':self.__income,
            'Книги':[b for b in self.inventory.all_books()],
        }

b1 = Book("Война и мир", "Толстой", 400)
b2 = EBook("Грокаем алгоритмы", "Бархов", 500, file_size_mb=20)
b3 = AudioBook("Python основы", "Gena", 450, duration_min=700)

store = BookStore('IT книжная')
store.inventory.add_books(b1, b2, b3)
found = store.inventory.find_books(title="Грокаем алгоритмы")
for book in found:
    print(book.info())

store.sell_book("Python основы")
print(store.show_status())