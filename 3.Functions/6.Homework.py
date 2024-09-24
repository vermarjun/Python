#QUESTION 1 VOLUME OF SPHERE 
def vol_sphere(r):
    volume = (4/3)*3.14*(r**3)
    return volume

print(vol_sphere(2))

#QUESTION 2 Number in RANGE
def number_range(num, low, high):
    return 5 <= high and 5>= low
print(number_range(5,2,7))
print(number_range(3,1,10))

#QUESTION 3 NO OF UPPER AND LOWER CASE LETTERS:
def up_low(sentance):
    up_count = 0
    low_count = 0
    for letter in sentance:
        if letter.isupper():
            up_count += 1
        elif letter.islower():
            low_count += 1
        else:
            pass
    print(f'No. of Lower case characters :{low_count}')
    print(f'No. of Upper case characters :{up_count}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

#QUESTION 4: Unique Element list
def unique_list(samp_list):
    return list(set(samp_list))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#QUESTION 5: Multiply all numbers in a list:
def multiply_list(list):
    product = 1 
    for element in list:
        product = element*product
    return product

print(multiply_list([1, 2, 3, -4]))

#QUESTION 6: Check Palindrome:
def check_palindrome(name):
    if name == name[::-1]:
        return True
    else: 
        return False

print(check_palindrome('helleh'))

#QUESTION 6: Check pangram:
import string
def check_pangram(word, alphabets = string.ascii_lowercase):
    list_alphabets = [letter for letter in alphabets]
    list_word = [letter for letter in word]
    for alphabet in list_alphabets:
        for letter in list_word:
            if alphabet == letter:
                continue
        
        
    

check_pangram('xyz')