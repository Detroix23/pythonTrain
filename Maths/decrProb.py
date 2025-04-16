
"""
PROBABILITY
Starts  at 0. Every itereration, x prob to stop and 1-0.5 prob to increase by 1
Yields "Number of time it landed on y by x"
"""

# Imports
import matplotlib.pyplot as plt
from random import *

def decrP(p = 1, x = 0.5):

    if x <= 0 or x > 1:
        return None
    for i in range(p + 1):
        e = -1
        r = 0
        while r != -1:
            e = e + 1
            r = random()
            if r <= x:
                r = -1

        yield e


def treatP(l = 1, p = 0.5):

    y = []
    for length in range(l + 1):
        y.append(0)

    for R in decrP(l, p):
        y[R] = y[R] + 1

    zero = True
    while zero:
        cz = len(y) - 1
        if y[cz] == 0:
            y.pop(cz)
        else:
            zero = False

    return y

def decrM(p = 1, x = 0.5):

    if x <= 0 or x > 1:
        return None
    for i in range(p + 1):
        e = 0
        r = 0
        while r != -1:

            r = random()
            e = e + 2 * (r-0.5)

            if r <= x:
                r = -1

        yield e

def treatM(l = 1, p = 0.5):

    r = {}
    x = []
    y = []

    for R in decrM(l, p):
        if R in r:
            r[R] = r[R] + 1
        else:
            r[R] = 1

    for v in r:
        x.append(v)
    for v in r:
        y.append(r[v])

    print()
    return x, y

def ui():
    c = input("Choose method (s, m): ")
    l = int(input("Number of iterations (positive int): "))
    p = float(input("Probability to stop (0:1): "))

    if c == "s":
        print("\n\bEntering in simple linear test")
        y = treatP(l, p)
        print("Results: ", y)
        plt.plot(y, 'ro')

    elif c == "m":
        print("\n\bEntering in bidirirectional test")
        x, y = treatM(l, p)
        print("Results: ", x)
        print("         ", y)
        plt.plot(x, y, 'ro')

    else:
        return ui()


    plt.show()
    input("Press Enter to go again...")

ui()





