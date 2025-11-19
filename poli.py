print(45+45) # сложение
print('hello'+"hello") # конкантенация

class Cat:
    def __init__(self, name):
        self.name = name 
    
    def sound(self):
        print("мяу-мяу")

class Dog:
    def __init__(self, name):
        self.name = name 
    
    def sound(self):
        print("гав-гав")

cat1 = Cat('Felix')
dog1 = Dog('Bobik')
for i in (cat1, dog1):
    print(i.sound())