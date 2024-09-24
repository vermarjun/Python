def input_int():
    #Note wheneven using true with while, you have to provide a break exit
    while True:
        #Try this code first = try
        #A try statement always has to be followed up with an except statement!
        try:
            result = int(input('Please input a number'))
        #If any error comes up way just execute the code below = Except
        except:
            print('Sorry Wrong input')
        #If no error and except is not executed for some reasons, this else statement is to be executed
        #Else and finally are kind of similar    
        else:
            print(f'Thanks your input is: {result}')
            break
        #No matter break or what, this finally (sucker) is !!ALWAYS!! executed.
        finally:
            print('Finally is always executed!')
            print('__________________________________________')

input_int()