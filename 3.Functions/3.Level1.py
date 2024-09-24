#QUESTION 1 OLD MCDOLNALD

def old_macdonald(x):
    letters_in_name = [letter for letter in x]
    letters_in_name[0] = letters_in_name[0].capitalize()
    letters_in_name[3] = letters_in_name[3].capitalize()
    name = ''
    for letters in letters_in_name:
        name = name + letters
    return name

#Check Post
ans = old_macdonald('macdonald')
print(ans)

#QUESTION 2 MASTER YODA

def master_yoda(sentance):
    words = sentance.split()
    backwards = words[::-1]
    sent = ''
    for word in backwards:
        sent = sent + word + " " 
    return sent
#Check Post
ans = master_yoda('I am home')
print(ans)
ans = master_yoda('We are ready')
print(ans)

#QUESTION 3 ALMOST THERE

def almost_there(n):
    if n <= 110 and n >= 90 or n <= 210 and n >= 190:
        return True
    else:
        return False
    
#Check Post
ans = almost_there(90)
print(ans)
ans = almost_there(104)
print(ans)
ans = almost_there(150)
print(ans)
ans = almost_there(209)
print(ans)