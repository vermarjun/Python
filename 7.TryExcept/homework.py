#QUESTION 1
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Fuck yeah mate, I've got some typefuckingerrors")
        #Note this break statement stops for loop from printing except and finally 3 times
        break
    finally:
        print('This cocksucker finally is executed always anyways fukcin muppet')

#QUESTION2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Dividing by Zero, are you schewpied')

#QUESTION3
def ask():
    while True:
        try:
            x = int(input('Enter a Number: '))
            ans = x**2
        except:
            print('That doesnt seem a valid input')
        else:
            print(ans)
            break
        finally:
            print('hey i am under the water here too much raining uwu')
ask()