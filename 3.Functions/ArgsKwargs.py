    ##  ARGS  ##
def my_func_args(*args):
    print(f'My name is {args[0]}') #Tuple is passed in as args
    print(f'My name is {args[1]}') #Tuple is passed in as args

my_func_args('Arjun', 'Verna', 'Golu') #No error shall be thrown irrespective of number of arguments that are passed in.

    ##  KWARGS  ##
def my_func_kwargs(**kwargs):
    print(f'My favourite fruit is {kwargs["fruit"]}')

my_func_kwargs(fruit='Apple')

    ## ARGS WITH KWARGS ##
def my_func_kwargs(*args,**kwargs):
    print(f'My name is {args[0]} and my favourite fruit is {kwargs["fruit"]}')

my_func_kwargs('Arjun',fruit='Apple')

# def myfunc1(my_string):
#     my_string3 = ''
#     for index,letter in enumerate(my_string):
#         if index % 2 == 0:
#             my_string3 = letter.append.capitalize()
#         else:
#             pass
#     return my_string
# my_string1 = 'arjun verma is handsome'
# string2 = myfunc1(my_string1)
# print(string2)

