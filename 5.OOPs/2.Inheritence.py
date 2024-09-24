class Animal():
    def __init__(self):
        print('Animal is created')
    def eat(self):
        print('Animal is eating')
    def who_am_i(slef):
        print('I am an Animal')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog is created')
    def eat(self): #Over writing existing method in base class
        print('Bobo is eating')
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cat is created')

Bobo = Dog()#Calling the object DOG will automatically print as defined
Tom = Cat()

Tom.eat() #This will print animal is eating as inherited from base class
Bobo.eat() #This will print BOBO is eating as base class's method has been overwritten by me in DOG class
Bobo.who_am_i() #This is will print i am animal for both objects which shows perfect use case for INHERITENCE!!!!


