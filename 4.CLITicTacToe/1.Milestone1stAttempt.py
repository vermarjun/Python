#Declarations
row0 = ['7','8','9']
row1 = ['4','5','6']
row2 = ['1','2','3']
dictionary_record = {'7':(row0,0),'8':(row0,1),'9':(row0,2),'4':(row1,0),'5':(row1,1),'6':(row1,2),'1':(row2,0),'2':(row2,1),'3':(row2,2)}

#Returns Choice of Player 1 and Player 2:
def welcome_message():
    print("Welcome to tic-tac-toe, Please use your keyboard's Num Pad as game board.")
    player_1 = 'Wrong'
    player_2 = 'Wrong'
    while  (player_1 != 'X') or (player_1 != 'O'):
        player_1 = input("Player 1 choose your symbol (X or O): ")
        if player_1 == 'X':
            player_2 = 'O'
            break
        elif player_1 == 'O':
            player_2 = 'X'
            break
        else:
            print('Wrong Input Try again.')
    return player_1,player_2

#Decide who goes first:
def first_turn(player_1_choice,player_2_choice):
    from random import randint
    randint1 = int(randint(1,10))
    randint2 = int(randint(1,10))
    first_turn = ''
    if randint1 >= randint2:
        first_turn = player_1_choice
    elif randint1 < randint2:
        first_turn = player_2_choice
        
    return first_turn

#PRINT TIC-TAC-TOE BOARD:
def display():
    row0= ['7','8','9']
    row1= ['4','5','6']
    row2= ['1','2','3']
    print(row0)
    print(row1)
    print(row2)
    return row0, row1, row2

#TAKE USER INPUT AND UPDATE BOARD, here value_of_cell should be X or O, should be returning rows with changed vlaues:
def update_board(row0, row1, row2, value_of_cell, dictionary_record):
    choice = 'Wrong'
    choice_range = range(1,10)
    while choice.isdigit() == False or choice in choice_range == False:
        choice = input('Choose a position according to number pad: ')
        choice = int(choice)
    choice = str(choice)
    x = dictionary_record[choice] #returns a tuple with row number and index
    # row_number = x[0]
    # col_number = x[1]
    x[0][x[1]] = value_of_cell #Represents cell that is to be changed
    return row0, row1, row2

# def decide_winner(row0, row1, row2, dictionary_record):
#     #Check row to be same
#     for item in row0:
#         if item == 'X':

#CHAINING ALL THE FUNCTIONS TOGETHER:
player_choices = welcome_message()
# print(player_choices)
# print(player_choices[0])
# print(player_choices[1])
player_1_choice = player_choices[0]
player_2_choice = player_choices[1]
ans = first_turn(player_1_choice, player_2_choice)
print(ans)


























# player_choice = welcome_message()
# print(player_choice)
