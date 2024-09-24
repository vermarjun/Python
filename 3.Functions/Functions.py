def name_snake_casing():
    '''
    Doc String
    '''
    print('Hello')

name_snake_casing()

def say_hello(name="Defult"):
    print(f'Hello {name}')

say_hello()
say_hello("Arjun")

def sum_num(num1, num2):
    return num1+num2

sum = sum_num(1,2)
print(sum)

def even_check(number):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

even_check(1)

#Return True if any number is Even inside a list
my_list = [1,3,3,3,5]

def check_list(list):
    for num in list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

ans = check_list(my_list)
print(ans)

#Return Even Numbers of the list:
my_list_even = [1,5,1,3,5]

def return_even_list(list):
    #Place holder variable
    even_numbers = []
    for num in list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    lenght_even_number_list = len(even_numbers)
    if lenght_even_number_list == 0:
        return 'No Even Numbers in list'
    else:
        return even_numbers


even_numbers = return_even_list(my_list_even)
print(even_numbers)