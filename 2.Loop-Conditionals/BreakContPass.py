#Pass => Acts as PlaceHolder for ex: this statement will not throw any error due to indenetation as of now.
for letter in "arjun":
    pass
#Break => Break out of loop
for letter in 'Arjun':
    if letter == 'u':
        break
    else:
        print(letter)
#Continue => Go to top of loop as soon as you find this condition
for letter in 'Arjun':
    if letter == 'u':
        continue
    else:
        print(letter) 
