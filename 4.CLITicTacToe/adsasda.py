# row0 = ['X','X','X']
# row_number = 0
# col_number = 1
# cell_to_change = row0[col_number]
# print(cell_to_change)
# print(type(cell_to_change))
# cell_to_change = 'x'
# row0[col_number] = 'x'
# print(row0)
# row0[1] = 'x'
# print(type(row0[1]))
# print(row0)
# dictionary_record = {'7':(row0,0),'8':(0,1),'9':(0,2),'4':(1,1),'5':(1,2),'6':(1,3),'1':(2,1),'2':(2,2),'3':(2,3)}
# choice = '7'
# x = dictionary_record[choice]
# value_of_cell = 2
# x[0][x[1]] = value_of_cell
# print(row0)
# def display(zz,zo,zt,oz,oo,ot,tz,to,tt):
#     # zz = ' '
#     # zo = ' '
#     # zt = ' '
#     # oz = ' '
#     # oo = ' '
#     # ot = ' '
#     # tz = ' '
#     # to = ' '
#     # tt = ' '
#     row00 = "      |      |      "
#     row01 = f'   {zz}  |   {zo}  |   {zt}  '
#     row02 = "______|______|______"
#     row10 = "      |      |      "
#     row11 = f'   {oz}  |   {oo}  |   {ot}  '
#     row12 = "______|______|______"
#     row20 = "      |      |      "
#     row21 = f'   {tz}  |   {to}  |   {tt}  '
#     row22 = "      |      |      "
#     print(row00)
#     print(row01)
#     print(row02)
#     print(row10)
#     print(row11)
#     print(row12)
#     print(row20)
#     print(row21)
#     print(row22)


# zz = ' '
# zo = ' '
# zt = ' '
# oz = ' '
# oo = ' '
# ot = ' '
# tz = ' '
# to = ' '
# tt = ' '
# # display(zz=' ',zo=' ',zt=' ',oz=' ',oo=' ',ot=' ',tz=' ',to=' ',tt=' ')
# display(zz,zo,zt,oz,oo,ot,tz,to,tt)

# def welcome_message():
#     print("WELCOME TO TIC-TAC-TOE (Use your keyboard's numpad as game board)")
#     player_1 = 'Wrong'
#     player_2 = 'Wrong'
#     while  (player_1 != 'X') or (player_1 != 'O'):
#         player_1 = input("Player 1 choose your symbol (X or O): ")
#         if player_1 == 'X':
#             player_2 = 'O'
#             break
#         elif player_1 == 'O':
#             player_2 = 'X'
#             break
#         else:
#             print('Wrong Input Try again.')
#     return player_1,player_2

# welcome_message()
# dispaly_dictionary = {'zz':'X','zo':'X','zt':'X','oz':'X','oo':'X','ot':'X','tz':'X','to':'X','tt':'X'}
# dispaly_dictionary2 = {'zz':' ','zo':' ','zt':' ','oz':' ','oo':' ','ot':' ','tz':' ','to':' ','tt':' '}
# # print(' ' not in dispaly_dictionary)
# # print(' ' not in dispaly_dictionary2)
# print(' ' not in list(value for value in dispaly_dictionary.values()))
# player_move = 100
# while (player_move in range(1,10)) == False:
#     player_move = input('Enter a number between 1-10: ')
# print(player_move)
# x = "Player1's Turn"
# y = x[0:7]
# print(y)