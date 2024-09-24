#QUESTION 1: SPY GAME
def spy_game(list):
    list_expected = [0,0,7]
    list_formed = []
    for num in list:
        if num == 0:
            list_formed.append(0)
        elif num == 7:
            list_formed.append(7)
        else:
            pass
    if list_formed == list_expected:
        return True
    else:
        return False   
            
#CHECK POST
ans = spy_game([1,2,4,0,0,7,5])
print(ans)
ans = spy_game([1,0,2,4,0,5,7])
print(ans)
ans = spy_game([1,7,2,0,4,5,0])
print(ans)

#QUESTION 2: COUNT PRIMES
def count_primes(num):
    Composite_Count = 0
    for integer in range(2,num+1):
        for x in range(2,integer):
            if integer % x == 0:
                Composite_Count += 1
                break
    Prime_Count = ((num+1)-(Composite_Count+2))
    return Prime_Count
       
#CHECK POST
ans = count_primes(100)
print(ans)

