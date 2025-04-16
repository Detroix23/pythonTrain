from random import *
import matplotlib.pyplot as plt 

def gen(M, R=50):
    x = 0
    h = 0
    i = []
    j = []
    go = True

    while x < R and go:
        
        r = randint(0, M)
        
        if r <= h and h != 0:
            h -= 1
        elif r > h and h != M:
            h += 1
        else:
            pass            
    
        #print(f"x: {x}; h: {h}")
        i.append(x)
        j.append(h)
        
        x += 1
        
    
    return i, j
        
        
i, j = gen(100000000)

print(i, j)   
    
plt.plot(i, j)

plt.show