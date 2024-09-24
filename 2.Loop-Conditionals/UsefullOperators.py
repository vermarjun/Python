#RANGE
for num in range(1,10,2):
    print(num)

#Enumerate
word = 'abcdef'
for index,letter in enumerate(word):
    print(letter, index)

#Zip 
##  EXAMPLE1    ##
my_list1 = [1,2,3,4,5,6,7]
my_list2 = ['a','b','c']
my_list3 = [100,200,300]
x = zip(my_list1, my_list2, my_list3)
for item in x:
    print(item)

##  EXAMPLE2    ##
y = zip('a,b,c,d',range(3),range(10))
print(list(y))

#IN  
print('a' in "arjun") #RETURNS TRUE
bool_x = 'x' in "arjun" 
print(bool_x) #RETURNS FALSE
print(1 in [1,2,3,4]) #RETURNS TRUE

#MinMax
my_list4 = [1,2,3,4,5,100,299]
print(min(my_list4)) #Prints 1
print(max(my_list4)) #Prints 299

#Random Library
#SHUFFLE LIBRARY
from random import shuffle
my_list5 = [1,2,3,4,5,6,7,100,299,499,566]
shuffle(my_list5) #Shuffles list randomly
print(my_list5)
#RANDOM INT LIBRARY
from random import randint
randominteger = randint(0,100)
print(randominteger)

#User Input
x = input('Enter a number: ')
print(x, type(x))
y = float(x)
print(y, type(y))
