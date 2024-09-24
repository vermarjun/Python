### COLLECTIONS MODULE ###
#1. COUNTER
from collections import Counter
my_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4]
my_sentance = 'I am arjun verma'
my_word = 'dfjkaashjkdfhasjlkfasdfhjaskdhfjkalsdhfajdfhasdhfsdfsjcbzbjcliahwfhjafjdsj'
c = Counter(my_list)
print(c)
#This will count letters in sentance
c = Counter(my_sentance) 
print(c)
#This will count words in sentance
c = Counter(my_sentance.split())
print(c)
c = Counter(my_word)
print(c)

#2. DEFAULT DICTIONARY
from collections import defaultdict
#Lambda is single use annonymous function which basically says that just assign 0 to values which are not defined
my_default_dict = defaultdict(lambda:'No')
#declaring a key value pair in dict just to see what is returned
my_default_dict['Correct'] = 'Yes'
print(my_default_dict['Correct']) #This will print Yes as declared
print(my_default_dict['Wrong']) #This key is not defined and hence will have default value as specified i.e 'No'

#3. NAMED TUPLE
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
Bobo = Dog(12, 'Indian', 'Bobo')
print(Bobo)
#These both will produce same output just as expected..
print(Bobo.age)
print(Bobo[0])
