#1) list declare
#1) shuffle list 
#2) user input
#3) shuffled list and user input passed in to check if they match!
#4) print result

my_list = ['','O','']

def shuffle_list(list_to_shuffle):
    from random import shuffle
    shuffled_list = shuffle(list_to_shuffle)
    return shuffled_list

def user_input():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Enter a Number 0, 1 or 2')
    return guess

def check_user_guess(shuffled_list, guess):
    if shuffled_list[guess] == 'O':
        print('Yay Right guess!')
    else:
        print('You lost!')
        print(shuffled_list)

shuffled_list = shuffle_list(my_list)
user_guess = user_input()
check_user_guess(shuffled_list, user_guess)