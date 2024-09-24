#1. YIELD()
#Like this i wont have to save data in a list to iterate over it or use it, NO USELESS MEMOMRY WASTAGE 
def yield_keyword(n):
    for x in range(n):
        yield x**3
for y in yield_keyword(10):
    print(y)

#2. NEXT()
def next_keyword():
    for x in range(3):
        yield x
g = next_keyword()
print(next(g))
print(next(g))
print(next(g))

#3. ITER()
s = 'Hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))