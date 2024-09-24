#QUESTION 1:
def square_num(num):
    for n in range(num):
        yield n**2
for x in square_num(10):
    print(x)

#QUESTION 2:
import random
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
