#QUESTION 1: LESSER OF 2 EVENS

def my_func1(x,y):
    #both are even
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            return x
        else:
            return y
    else:
        if x > y:
            return x
        else:
            return y
        
#Check point
ans = my_func1(2,4)
print(ans) #returns 2
ans = my_func1(2,5)
print(ans) #returns 5

#QUESTION 2: ANIMAL CRACKERS

def my_func2(x):
    y = x.split()
    if y[0][0] == y[1][0]:
        return True
    else:
        return False 
#Check Point
ans = my_func2('Levelheaded Llama')
print(ans)
ans = my_func2('Crazy Kangaroo')
print(ans)

#QUESTION 3: MAKES TWENTY

def my_func3(x,y):
    if x == 20 or y == 20 or x+y == 20:
        return True
    else:
        return False
#Check Point
ans = my_func3(20,10)
print(ans)
ans = my_func3(12,8)
print(ans)
ans = my_func3(2,3)
print(ans)

