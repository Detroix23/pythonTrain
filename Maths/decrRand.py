
from random import *
import matplotlib.pyplot as plt


def decrRandom(a=0, b=0, c=0, l0=None):
    """
    Parameters
    ----------
    a, b, c : parmaters for the quadratic recursive. Default is 0.
    l0 : start value for the recursive. 
    Be sure that the function will tend to 0, or will never end
    Default is 1.

    Returns
    -------
    ls : List of all values of s (purpose: x)
    ll : List of all values of l

    """
    # Vars
    r = random()
    if type(l0) == int or type(l0) == float:
        l = l0
    else:
        l = 1
    s = 0
    ls = [s]
    ll = [l]
    run = True
    
    # Main
    while r < l and s < 10000 and run:
        s += 1
        ## Update l, according to l0 (recursive or function)
        if type(l0) == int or type(l0) == float:
            l = a * l ** -2 + b * l + c
        else:
            l = a * s ** -2 + b * s + c
        
        r = random()
        
        if l < 0 or l > 1:
            run = False
        else:
            ls.append(s)
            ll.append(l)
    

    
    return ls, ll

ls, ll = decrRandom(-0.001, -0.1, 1.000001)

print(ls[-1])
print("l=", [round(y, 3) for y in ll])

plt.axis()
plt.title(f"Limit l for values of s. Result: {ls[-1]}")
plt.xlabel("X: values of s")
plt.ylabel("Y: values of l")
plt.plot(ls, ll)
plt.show()

