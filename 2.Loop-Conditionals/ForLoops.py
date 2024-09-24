my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)

#Printing Even Numbers:

for num in my_list:
    #Check if even
    if (num%2 == 0):
        print(num)

#Sum of all numbers in list:
my_list_sum = 0
for num in my_list:
    my_list_sum = my_list_sum + num 
print(my_list_sum)

#Letters of string via for loops
my_string = 'Hello World'
for letter in my_string:
    print(letter)
#Iterating through tuple:
my_tuple = (1, 2, 3)
for tup in my_tuple:
    print(tup)

#Tuple Unpacking:
my_tup_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in my_tup_list:
    print(a)
for a,b in my_tup_list:
    print(a,b)
for a,b in my_tup_list:
    print(a)
    print(b)

#Iterating Through Dictionaries:
my_dict = {'key1':1, 'key2':2, 'key3':3}
#By Default will print keys only
for key in my_dict:
    print(key)
#To access key value pairs:
for key_value_pairs in my_dict.items():
    print(key_value_pairs)
#To access values:
for key,value in my_dict.items():
    print(value)
#To access keys:
for key,value in my_dict.items():
    print(key)