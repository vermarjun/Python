#   Questions left till now : numbers question1, lists question 1

##  NUMBERS ##

#QUESTION 1
#Numbers: store numerical info, 2 types: int and float
#Strings: ordered sequence of characters
#Lists: ordered mutable sequence to store any data type 
#Tuples: ordered immutable sequence of objects
#Dictionaries: undered key value mapping

#QUESTION2
x = (100+(1/4))*(1**1)/1
print(x)

#QUESTION3
x = 4*(6+5)
print(x)
x = 4*6+5
print(x)
x = 4+6*5
print(x)

#QUESTION4
print(type(3+1.5+4))

#QUESTION5
#1) SquareRoot 
#Method 1
x = 4**(1/2)
print(x)
#Method 2
x = pow(4, 1/2)
print(x)
#Method 3
import math
x = math.pow(4, 1/2)
print(x)

#2) Square 
#Method 1
x = 4**(2)
print(x)
#Method 2
x = pow(4,2)
print(x)
#Method 3
import math
x = math.pow(4,2)
print(x)

## STRINGS ##

#QUESTION 1
s = "hello"
print(s[1])

#QUESTION 2
print(s[::-1])

#QUESTION 3
print(s[4])
print(s[-1])

## LISTS ##

#QUESTION 1
#Method 1
my_list = [0, 0, 0]
print(my_list)
#Method 2
my_list2 = [0]*3
print(my_list2)

#QUESTION 2
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

#QUESTION 3
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

##  DICTIONARIES ##

#QUESTION 1
d = {'simple_key':'hello'}
print(d['simple_key'])

#QUESTION 2
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

#QUESTION 3
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

#QUESTION 4
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#QUESTION 5
#No You Cannot sort a dictionary because dict are mappings and do not maintain or retain any order

##  TUPLES  ##
#QUESTION 1
#1) Tuples are immutable while list are mutable, ie values of tuples cannot be reassigned!
#2) Methods associated with tuples are very less compared to lists

#QUESTION 2
my_tuple= (1, 2, 3, 1)
print(my_tuple.count(1))
print(my_tuple.index(1))

##  SETS    ##
#QUESTION 1
#Values cannot repeat in a set, unordered colllection of unique elemenets = sets. 

#QUESTION 2
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

##  BOOLEANS    ##
#QUESTION 1
print(2 > 3) #False
#QUESTION 2
print(3 <= 2) #False
#QUESTION 3
print(3.0 == 3) #True
#QUESTION 4
print(4**0.5 != 2) #False
#QUESTION 5
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1']) #False