# 1) Declaring functions as VARIABLES!!
def hello():
    return 'Hey i am a func'

print(hello)
print(hello())
greet = hello #Declaring a function as a variable
print(greet()) #This will work same as hello function
del hello #Deleting hello function
print(greet()) #Even if a delete hello() greet will still work because greet create an entirely new func on assignment instead pointing to hello function!

# 2) Passing function inside function as argument
def passing_in_func_as_argument():
    return 'I am function that has been passed in main() func as argument!'
def main(passing_in_func_as_argument): #Passing in function as argument
    print('Main func starting')
    x = passing_in_func_as_argument() #Calling the passed in function
    print(x)
    def sub1():
        return 'I am sub1() func inside main() func I was returned'
    def sub2():
        return 'I am sub2() func inside main() func'
    print('Main func ends here') 
    return sub1  #Returning a function

returned_func = main(passing_in_func_as_argument)
print(returned_func())

# 3) Decorators
def decorator(function_that_wants_to_be_decorated):
    def wrapper_func():
        print('Code running before ')
        function_that_wants_to_be_decorated()
        print('Code running after')
    return wrapper_func
#Function that has to be decorated, hence passed in decorator function
def func_needs_decorator():
    print("This function is in need of a Decorator")
#Function before decoration
func_needs_decorator()
decorated_func = decorator(func_needs_decorator)
#Decorated function 
decorated_func()

#This method of passing in function in decorator function to be decorated is simplified by using '@' symbol!
@decorator
def func_needs_decorator():
    print('This function is in need of a Decorator"')
func_needs_decorator()