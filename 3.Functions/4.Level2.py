#QUESTION 1) FIND 33:
def find_33(arr):
    for index,num in enumerate(arr):
        if index == 0:
            if num == 3:
                if arr[index+1] == 3:
                    return True
                else:
                    return False
            else:
                pass
        elif index == -1:
            if num == 3:
                if arr[index-1] == 3:
                    return True
                else:
                    return False
            else:
                pass
        else:
            if num == 3:
                if arr[index-1] == 3 or arr[index+1] == 3:
                    return True
                else:
                    return False
            else:
                pass

#CHECK POST:
ans = find_33([1,3,3])
print(ans)  #True
ans = find_33([1,3,1,3])
print(ans)  #False
ans = find_33([3,1,3])
print(ans)  #False

#QUESTION 2) PAPER DOLL:
def paper_doll(string):
    string_split = [letter for letter in string]
    string_split = [letter*3 for letter in string_split]
    string = ''
    for letter in string_split:
        string = string + letter
    return string

#CHECK POST:
ans = paper_doll('Hello')
print(ans) 
ans = paper_doll('Mississippi')
print(ans)

#QUESTION 3) BLACK JACK:
def black_jack(x,y,z):
    sum = x+y+z
    if sum <= 21:
        return sum
    elif sum > 21:
        if x == 11 or y == 11 or z == 11:
            sum = sum - 10
            return sum
        else: 
            return 'BUST'

#CHECK POST:
ans = black_jack(5,6,7)
print(ans) 
ans = black_jack(9,9,9)
print(ans) 
ans = black_jack(9,9,11)
print(ans) 

#QUESTION 4) SUMMER OF 69:
def summer_69(arr):
    sum = 0
    for num in arr:
        if num <=9 and num >=6:
            pass
        else:    
            sum = sum + num       
    return sum


#CHECK POST:
ans = summer_69([1,3,5])
print(ans) 
ans = summer_69([4, 5, 6, 7, 8, 9])
print(ans) 
ans = summer_69([2, 1, 6, 9, 11])
print(ans) 




