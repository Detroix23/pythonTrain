import random as random
import os
import time as t

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def inputint(t):
    pass


def init():
    
    global m
    
    #Intro
    print("-")
    print("Hello and welcome to Skibidi Gambling Ultimate GYATT Edition")
    print("-")
    t.sleep(1)
    
    ##initial funds
    
    print("Choose you initial funds")
    while True:
        try:
            m = float(input())
            if m <= 0:
                print("Warning - Cannot pick {} as starting money. Please try again".format(m))
            else:
                break
        except ValueError:
            print("Warning - Wrong input, not an integer. Please try again". format(m))

    print("You start with {} $".format(m))

    #Continue
    input("Press Enter to go to hub...")
    print("-")
    return hub()


def hub():
    global m
    global c
    global ctTf
    

    
    #Check loose condition
    if m <= 0:
        print("-")
        print("You lost!\nYou spent on your money in gambling and now you have to live in the street !")
        print("Restarting...")
        t.sleep(2)
        return init()

    print("\nHUB\nType the number that belong respectivelly to your game !")
    t.sleep(0.2)
    print("-")
    print("0 - Look your available money")
    t.sleep(0.1)
    print("1 - History logs")
    t.sleep(0.1)
    print("2 - Tails or Faces")


    #Choose game
    while True:
        try:
            c = int(input())
            break
        except ValueError:
            print("Warning - Wrong input, not an integer. Please try again". format(c))

    if c == 0:
        cls()
        t.sleep(0.1)
        print("You have actually {} $ in your wallet".format(m))
        print("You played {} games".format(ctTf))
        input("Press Enter to go back to hub...")
        return hub()
    
    elif c == 1:
        return logs()
    
    elif c == 2:
        return tf()
    
    else:
        print("Warning - Wrong input ({}), out of bounds. Sending back to hub". format(c))
        return hub()
    

    
def logs():
    if logTf == {}:
        print("Warning - No Tails and Faces logs")
    else:
        print("History of Tails and Faces\n",logTf)
    
    input("Press Enter to go to hub...")
    print("-")
    return hub()



def tf():

    global ctTf
    global m
    print("You choose TAILS OR FACE !")
    print("Your bid is doubled if you roll Tails, but you loose it all if Heads...")
    t.sleep(0.2)
    
    
    #Gamble

    print("\nYou have {} $. How much do you gamble ? (enter 'max' to all in)".format(m))

    while True:
        g = input()
        if g == "max":
            g = m
            print("ALL IN WITH {} $!".format(g))
            break
        try:
            g = float(g)
            if g>m:
                print("Warning - Wrong input, you do not have {} $, you have only {} $. Please try again".format(g,m))
            elif g<=0:
                print("Warning - Wrong input, you cannot bid {}. Please try again".format(g))
            else:
                break
        except ValueError:
            print("Warning - Wrong input not an integer. Please try again")

    #Game + logs (1 = win, 0=loose)
    print("Loading...")
    t.sleep(0.9)
    if random.randint(0, 1)==1:
        print ("Tails ! You won {} $".format(g))
        m = m + g
        logTf[ctTf] = 1
    else:
        print("Heads ! You lose {} $".format(g))
        m = m - g
        logTf[ctTf] = 0
    
    t.sleep(0.2)
    print("You exit with {} $".format(m))
    
    #Exit
    ctTf = ctTf +1
    return hub()

    



#Init

##BEGGINING

#cls()
t.sleep(0.1)

##Variables
c = 0
m = 0
###Logs
logTf = {}

###Counters (of how many time game played)
ctTf = 0


#Orders
init()
print("Error - Program Exited")



