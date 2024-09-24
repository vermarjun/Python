##ADVANCED NUMBERS
print(hex(1024)) #Converting to hex
print(bin(1024)) #Converting to binary
print(round(5.23222,2))

##ADVANCED STRINGS
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

##ADVANCED SETS
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1.intersection(set2))

##ADVANCED DICTIONARIES
#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
print({x:x**3 for x in range(5)})

##ADVANCED LISTS
list1 = [1,2,3,4]
print(sorted(list1))
list2 = [3,4,2,5,1]
list2.reverse()
# list2.sort()
print(list2)