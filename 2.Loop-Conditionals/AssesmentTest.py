#QUESTION 1
st = 'Sam Print only the words that start with s in this sentence'
my_list = st.split()
for letter in my_list:
    if letter[0].lower() == 's':
        print(letter)
    else:
        continue

#QUESTION 2
for x in range(0,11,2):
    print(x)

#QUESTION 3
my_list3 = [x for x in range(1,50) if x%3 == 0]
print(my_list3)

#QUESTION 4
st = 'Print every word in this sentence that has an even number of letters'
sent = st.split()
for word in sent:
    letter_count = 0
    for letter in word:
        letter_count += 1
    if letter_count%2 == 0:
        print('Even')
    else:
        continue

#QUESTION 5
for num in range(1,100):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)

#QUESTION 6
st = 'Create a list of the first letters of every word in this string'
word = st.split()
print(word)
my_list2 = [y for x in word for y in x[0]]
print(my_list2)