def user_input():
    #Conditions to check:
    #1) Input in acceptable range?
    #2) Input is number or not?
    #Initals
    choice = 'Wrong'
    acceptable_range = range(0,11)
    within_range = False

    #While loop to be executed as long as input is as expected:
    while choice.isdigit() == False or within_range == False:
        choice = input('Enter a number between (0-10): ')
        
        #Digit Check
        if choice.isdigit() == False:
            print('I said enter a number ,you muppet!')
        
        #Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Dumb shit, I said enter a number between 0-10')
    return int(choice)

ans = user_input()
print(ans)  