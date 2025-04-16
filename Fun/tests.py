# TEST & TRAINING FILE
import matplotlib.pyplot as plt

## Try except
def t_try():
    c = str(5)
    print(type(c))

    try:
        int(c)
        print("Ok")
    except ValueError:
        print("Error")

    print("Finish")


## Trying to learn classes
l1 = []
c1 = 0

class mark:
    def __init__(self, name, note):
        self.name = name
        self.note = note


    def __str__(self):
        return f"{self.name} obtained {self.note}"


## Finding out which is the best suite for the garlatti suite

def gar(z):
    g = 1
    h = 2
    i = 3
    j = 0

    l = [1, 2, 3]
    c = 0

    while j < z:
        ## Base calcul & save result
        j = (h * i) / (g * i)
        l.append(j)


        ## Offset all variables
        g = h
        h = i
        i = j
        c = c + 1

    print(l)
    plt.plot(l)

    plt.show()

gar(10)



## Test for Fall of 1

class Rpos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The robot is situated in x = {self.x} and y = {self.y}"

    def ask(self):
        return int(self.x), int(self.y)

def fun(a, b):
    Rpos.x = a
    Rpos.y = b
    print(Rpos.x, Rpos.y)

fun(1,2)