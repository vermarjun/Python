def myfunc(string):
    #Converting string to list
    letter_list = [letter for letter in string]
    for list_index in range(0,len(letter_list)):
        if list_index % 2 == 0:
            letter_list[list_index] = letter_list[list_index].capitalize()
        else:
            letter_list[list_index] = letter_list[list_index].lower()
    #Declaring string
    list_to_string = ''
    for letter in letter_list:
        # print(index)
        list_to_string = list_to_string + letter
    return list_to_string

print(myfunc("fook yeah it's working lads!"))
