dispaly_dictionary = {'zz':' ','zo':' ','zt':' ','oz':' ','oo':' ','ot':' ','tz':' ','to':' ','tt':' '}
#Returns Choice of Player 1 and Player 2:
def welcome_message():
    print("WELCOME TO TIC-TAC-TOE (Use your keyboard's numpad as game board)")
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

#Take inputs :
#Returns numerical choice of player EX: 1,7,9 etc
def player_input(whose_turn):
    print(f"{whose_turn}: ")
    # player_move = 100
    # while (player_move in range(1,10)) == False:
    player_move = input('Enter a number between 1-10: ')
    return player_move

#Keyword choice :
#Converts numerical choice to keyword choice EX: zz,oz,to,ot etc
def player_move_dict(player_move):
    player_move_dict = {'7':'zz','8':'zo','9':'zt','4':'oz','5':'oo','6':'ot','1':'tz','2':'to','3':'tt'}
    return player_move_dict[player_move]

#Turn decider :
#Returns whose turn it is by modulo current move by 2
def whose_turn_decider(current_move):
    if current_move%2 == 0:
        return "Player1's Turn"
    elif current_move%2 != 0:
        return "Player2's Turn"
    
#Dictionary to decide which move is to be made:
#WILL RETURN UPDATED DICTIONARY WHICH HAS PLAYER DISPLAY POSITION MOVES
def display_move_dictionary(whose_turn,player_1_choice,player_2_choice,player_move_position,dispaly_dictionary):
    if whose_turn ==  "Player1's Turn":
        dispaly_dictionary[player_move_position] = f'{player_1_choice}'
    elif whose_turn == "Player2's Turn":
        dispaly_dictionary[player_move_position] = f'{player_2_choice}'
    return dispaly_dictionary
   
#DECIDING WINNER:
def winner_decider(updated_display_dictionary):
    we_have_a_winner = False
    # DIAGONAL CONDITION
    if updated_display_dictionary['zt'] == updated_display_dictionary['oo'] == updated_display_dictionary['tz'] != ' ':
        we_have_a_winner = True
    #REVERSE DIAGONAL CONDITION
    if updated_display_dictionary['zz'] == updated_display_dictionary['oo'] == updated_display_dictionary['tt'] != ' ':
        we_have_a_winner = True
    #ROW CONDITION    
    elif (updated_display_dictionary['zz'] == updated_display_dictionary['zo'] == updated_display_dictionary['zt'] != ' ') or (updated_display_dictionary['oz'] == updated_display_dictionary['oo'] == updated_display_dictionary['ot'] != ' ') or (updated_display_dictionary['tz'] == updated_display_dictionary['to'] == updated_display_dictionary['tt'] != ' '):     
        we_have_a_winner = True
    #COLOUMN
    elif (updated_display_dictionary['zz'] == updated_display_dictionary['oz'] == updated_display_dictionary['tz'] != ' ') or (updated_display_dictionary['zo'] == updated_display_dictionary['oo'] == updated_display_dictionary['to'] != ' ') or (updated_display_dictionary['tz'] == updated_display_dictionary['ot'] == updated_display_dictionary['tt'] != ' '):     
        we_have_a_winner = True
    return we_have_a_winner

#Display function, prints out board into terminal, just pass in the values of variables
def display(dispaly_dictionary):
    zz = dispaly_dictionary['zz']
    zo = dispaly_dictionary['zo']
    zt = dispaly_dictionary['zt']
    oz = dispaly_dictionary['oz']
    oo = dispaly_dictionary['oo']
    ot = dispaly_dictionary['ot']
    tz = dispaly_dictionary['tz']
    to = dispaly_dictionary['to']
    tt = dispaly_dictionary['tt']
    row00 = "      |      |      "
    row01 = f'   {zz}  |   {zo}  |   {zt}  '
    row02 = "______|______|______"
    row10 = "      |      |      "
    row11 = f'   {oz}  |   {oo}  |   {ot}  '
    row12 = "______|______|______"
    row20 = "      |      |      "
    row21 = f'   {tz}  |   {to}  |   {tt}  '
    row22 = "      |      |      "
    print(row00)
    print(row01)
    print(row02)
    print(row10)
    print(row11)
    print(row12)
    print(row20)
    print(row21)
    print(row22)

#Game can have max 9 turns, depending on current turn i can decide who's turn it must be now
current_turn = 0
#welcome message and get player choice as X or O
player_choices = welcome_message()
player_1_choice = player_choices[0] 
player_2_choice = player_choices[1]

#Decide Whose turn is it now:
whose_turn = whose_turn_decider(current_turn)

#Take input of where player wants to play:
player_move = player_input(whose_turn)

#Map this move to get position of move in keyword format:
player_move_position = player_move_dict(player_move) #This will just give me postion at which player want to play in format of zz ,zo ,oz, tz etc
# print(player_move_position)

#Passing all the required variables into display_dictionary which will be updated based on variables being passed and return that updated dictioary!
updated_display_dictionary = display_move_dictionary(whose_turn,player_1_choice,player_2_choice,player_move_position,dispaly_dictionary)
display(updated_display_dictionary)
winner = winner_decider(updated_display_dictionary)
while winner == False:
    current_turn += 1
    whose_turn = whose_turn_decider(current_turn)
    player_move = player_input(whose_turn)
    player_move_position = player_move_dict(player_move)
    updated_display_dictionary = display_move_dictionary(whose_turn,player_1_choice,player_2_choice,player_move_position,dispaly_dictionary)
    display(updated_display_dictionary)
    winner = winner_decider(updated_display_dictionary)
    #If winner_decider returns True that is we have a winner, so print who won before wwhile loop ends
    if winner == True:
        winner_string = whose_turn[0:7] #Whose turn se string extract ki to declare winner
        print(f'{winner_string} WON!')
    #Incase we dont have any winner, this if statement declares TIE!
    if ' ' not in list(value for value in dispaly_dictionary.values()):
        print('MATCH TIED!')
        break

