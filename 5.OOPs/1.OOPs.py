class Dog():
    #CLASS ATTRIBUTES => irrespective of instances
    species = 'Mamals'
    #INSTANCE ATTRIBUTES 
    #Instance Attributes dont have ()
    def __init__(self,breed,name,spots,age,cute):
        self.breed_attribute = breed
        self.name_attribute = name
        self.spots_attribute = spots
        self.age_attribute = age
        self.cute_attribute = cute
    #METHODS => Methods are just functions inside OBJECTS!
    #Methods have (), When you call them:
    def bark(self): #Note here self keyword is connecting this method with rest of the object!
        print('Woof Woof my name is {}'.format(self.name_attribute))
    #Note we can also pass in other inputs than inside the method, providing them at the time of call  
    def bark_the_number(self,number): #Note here self keyword is connecting this method with rest of the object!
        print('Woof Woof my name is {} and the number you provided is {}'.format(self.name_attribute,number))

my_dog = Dog(breed='Indian', name='Bobo', spots=False, age=12, cute=True)
print(my_dog.breed_attribute)
print(my_dog.name_attribute)
print(my_dog.spots_attribute)
print(my_dog.age_attribute)
print(my_dog.cute_attribute)
my_dog.bark()
my_dog.bark_the_number(number=9)

#EXAMPLE CREATING A OBJECT TO CALCULATE AREA/PERIMETER OF A CIRCLE:
class circle():
    # CLASS OBJECT ATTRIBUTES
    pi = 3.14 #Since the fact that pi is 3.14 will never change at any instance!
    #INSTANCE ATTRIBUTES
    def __init__(self,radius=1): #Note here radius = 1 is default value for just in case what if radius is not passed in.
        self.radius = radius
    def area(self):
        print(self.pi*(self.radius**2))
    def perimeter(self):
        print(self.pi*(self.radius)*2)

my_circle = circle(radius=10)
print(my_circle.radius)
my_circle.area()
my_circle.perimeter()