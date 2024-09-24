a = 5
print(a+a)
String_Name = "abcdefghi" #Assigning value to a variable
print(type(String_Name)) #Printing type of variable
print(String_Name) #Printing variable storing string
print(len(String_Name)) #Length
print(String_Name[0]) #Indexing
print(String_Name[-1]) #Reverse Indexing
print(String_Name[1:]) #Slicing, STARTING INDEX
print(String_Name[:2]) #Slicing, END INDEX
print(String_Name[1:2]) #Slicing, COMBINING BOTH
print(String_Name[::2]) #Slicing, Stepping 2 characters

# Better way of doing from line 7 to 12 would be:
print("abcdefghi"[0])

#CONCATENATION
last_name = "Verma"
name = "Arjun "+ last_name
print(name)
print(name*3) #Prints name 3 times

#METHOD
print(name.upper()) #All Letter uppercase
print(name.lower()) #All Letter Lowercase
print(name.split()) #ALL words split apart in list
print(name.split("r")) #ALL a form name will be removed

#F-strings: formatting strings
print("This is a string {} {} {}".format("fox", "brown", "quick")) 
print("This is a string {0} {0} {0}".format("fox", "brown", "quick")) #REPEATING
print("This is a string {2} {0} {1}".format("fox", "brown", "quick")) #Deciding with indexes
print("This is a string {f} {s} {t}".format(f="fox", s="brown", t="quick")) #Using Variables

#.format() Method
result = 100/777
print("Result is {r}".format(r=result)) #This prints a big number, to edit this number to some specific decimal places we will use
print("Result is {r:1.3f}".format(r=result)) #This prints a big number, to edit this number to some specific decimal places we will use

#LISTS
#note: lists can store mutlipe data types
my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len(my_list1) #10
my_list1[0] #0
my_list1[1:] #[2,3,4,5,6,7,8,9]
my_listnew = my_list1+ my_list2 #sum of both the lists, concatenating 2 lists together
my_list1[0]="a" #Assigns value a to 0th position in my_list1 instead of 0
my_list1.append(10) #Add Items to the list
print(my_list1)
my_list1.pop(0) #Delete items from list
#Note : popping element also returns the element that has been popped
poppedElement = my_list1.pop(0)
print(my_list1)
print(poppedElement)
my_list1.reverse() #will reverse the order of values inside the list
print(my_list1)
my_list1.sort() #will sort the list in order
print(my_list1)

#Dictionaries
my_dict = {"key1":"value1", "key2":"value2"}
print(my_dict["key1"]) #Prints value1
d = {"k1":123, "k2":[1, 2, 3], "k3":{"inside_key":100}, "k4":['a', 'b', 'c']} #keys can have int var dict and lists as values
print(d["k1"], d["k2"], d["k3"])
print(d["k2"][1]) #Prints 2
print(d["k4"][2].upper()) #Prints uppercase C
d["k2"].reverse() #Reverses k2 ie 3 , 2, 1
print(d["k2"]) 
d["k5"] = [5, 4, 3, 2, 1] #Add new key k5 with specified value to dict d
print(d["k5"])
d["k1"] = "Arjun" #Assign new value Arjun to k1
print(d["k1"])
print(d.keys()) #prints all keys of d
print(d.values()) #prints all values of d 
print(d.items()) #prints all items of d

#Tuples
t = ('a', 'a', 'b', 'c', 'd')
print(t[0])
print(t[-1])
print(t.count('a')) #Prints how many times a is repeating
# t[0] = 'c' will throw an error because tuples are immutable
print(t.index('c')) #prints the first occurance of c

#Sets
myset = set()
myset.add(1)
print(myset)
myset.add(3)
print(myset)
myset.add(3) #Adding 3 again to set will not work because set has unique elements 
print(myset)
print(set("arjun verma")) #will only print non repeating elements and not in any order => {'e', 'a', 'n', 'u', 'm', 'v', 'j', ' ', 'r'}
mylist = [1,2,2,2,23,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,45,5,5,5,5,5,5,5,5]
myset = set(mylist)
print(myset) #Will print values only one time in the repeating list

#Open and Read Files with python
myfile = open("E:\\5) Python\\UdemyLecs\\Section3\\file1.txt")
print(myfile.read())
myfile.close() #Always close files so that you dont get error if you ever try to rename or delete it in reallife 

#Open files in other directory:
myfile2 = open("E:\\5) Python\\UdemyLecs\\myfile.txt")
print(myfile2.read())
myfile2.close() 

#Better Way:
with open('E:\\5) Python\\UdemyLecs\\myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

#Creating a file with python. This method uses mode write with which it creates a new file if file specified is not found else if the file is found then it
#replaces the file with new file
with open('E:\\5) Python\\UdemyLecs\\myfile3.txt', mode='w') as my_new_file3:
    my_new_file3 = "arjun"
print(contents)

