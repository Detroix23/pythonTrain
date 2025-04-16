from random import *


al = [chr(c) for c in range(97, 123)]

w = randint(1,10)
lW = []

for word in range(w):
    l = randint(1, 25)
    tempW = []
    for length in range(l):
        r = randint(0,25)
        
        for letter in range(r):
            tempW.append(al[letter])
    
    lW.append(tempW)


print(lW)
