#MAP
def square(num): #function
    return num**2
my_list = [1,2,3,4,5,6] #Iterable

square = list(map(square, my_list)) #Storing value
print(square)

#FILTER
def even(num): #function
    return num%2 == 0 #returns True or False
my_list = [1,2,3,4,5,6]

even = (list(filter(even, my_list))) #Only returns values that were returned as True by function
print(even)