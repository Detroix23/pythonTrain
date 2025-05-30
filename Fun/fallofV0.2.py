""""
FALL OF
 This script consist, in short, to compute the probability, over r iteration, of a little robot on a x by y grid
 to reach to border or one or more 'exits'
 in n number of moves while it has an equiprobabilty of heading in each cardinal directions
 Here a 'win' is when the bot exited the room ( P(e) = N(exits) / R
"""

# Imports
import random
import time as t
# Classes


class Rpos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The robot is situated in x = {self.x} and y = {self.y}"

    def ask(self):
        return int(self.x), int(self.y)

# Functions

def init():
    # The start of the UI


    ## Go to hub
    return hub()



def hub():
    # Hub function that serves as a central point where scripts can get back here if needed or if they reach their end

    ## Variable calls
    global vi
    uc = "" ### User choice


    print("\nHub")
    print("Choose between (vi) for toggling visual yields, (go) to initialize main function")
    uc = input("String input: ") ### User choice

    if uc == "vi":
        if vi is True:
            vi = False
            print("Set vi to False. Visual returns turned off")
        else:
            vi = True
            print("set vi to True. Visual returns are on")
        input("Press Enter to go back to hub...")
        return hub()

    elif uc == "go":
        print("Starting main function")
        return run()

    else:
        print("Warning - Invalid input. Starting anyway main function")
        return run()
    ##

def grid():
    # Grid setup function

    ## Variable calls
    global vi, lx, ly, stx, sty

    viG = []

    ## User choice + verification of input + starting point
    print("\nGrid setup")
    print("Please choose the dimension of the grid (preferably odd numbers)")
    while True:
        try:
            lx = int(input("X: "))
            ly = int(input("Y: "))
            if lx < 1 or ly < 1:
                raise ValueError
            break
        except ValueError:
            print("Warning - At least one invalid input ({}, {}), please try again".format(lx, ly))

    ### Starting point calculation

    stx = int(-(lx // -2))
    sty = int(-(ly // -2))
    print("The script tries to automatically find the middle point if there's one. It found {}; {}. Correct them manually or valid by hitting Enter two time".format(stx, sty))
    try:
        stx = int(input("(Enter to skip...) Starting X: "))
        sty = int(input("(Enter to skip...) Starting Y: "))
    except ValueError:
        print("Skipped")
    print()

    ## Return to user
    print("You have chosen a grid of dimension x = {} and y = {}".format(lx, ly))
    print("The bot will start at x = {} and y = {}".format(stx, sty))

    ## Visual interpretation (w/ starting point)
    if vi == True:
        for y in range(1, ly+1):
            for x in range(1, lx+1):
                if x == stx and y == sty:
                    print("0", end=" ")
                else:
                    print("*", end=" ")
            print()


def results(r, n, cw, tStart, tEnd):
    ## Variables
    ts = 0 ### Temp sum variable to calculate average

    ## This function will interprete the results (maybe expand later)
    print("\nResults")
    print(f"Program took {round(tEnd - tStart, PRN)} seconds to execute")
    print(f"Over {r} iterations total and whilst the bot had {n} moves, it managed to fall of {len(cw)} times")
    print(f"The probability of the bot falling of was of {len(cw)/ r}")

    ##More in depth
    ### Print cw
    if vi == True:
        print("Wins in for (iteration): (tries)")
        for key, value in cw.items():
            print(f"{key}: {value}", end="; ")
        print()

    ### Average number of tries to win
    for key, value in cw.items():
        ts += int(value)
    print(f"The bot needed in average {round(ts/len(cw),PRN)} moves to fall of")


def run():
    # Actual program

    ## Variables
    global lx, ly, stx, sty, cw, vi, tStart, tEnd

    r = 0    ### Iterations total
    n = 0    ### Number of maximum moves
    dt = 0   ### Random int between 1 and 4 that choose the direction of the bot (same probability to go to one of the 4 cardinal directons
    px = 0   ### Pos x of the bot
    py = 0   ### Pos y of the bot

    ## Setup parameters with other functions
    print("You ran the test. Please set the following paramters")
    grid()
    print("\nBot setup")
    while True:

        try:
            print("Please set the maximum amount of move that the bot is allowed to do")
            n = int(input("Max moves n: "))
            print("Please set the number of iteration that the script will go through")
            r = int(input("Iterations r: "))

            break

        except ValueError:
            print("Warning - Invalid input: not an integer ({} or {})".format(n, r))

    print("The test will execute {} times, in a {} by {} grid where the bot start at {};{} and has a maximum of {} moves\n".format(r, lx, ly, stx, sty, n))


    ## Main loop

    ### Start timer
    tStart = t.time()

    for i in range(1, r+1):
        px = stx
        py = sty
        for j in range(1, n+1):
            dt = random.randint(1,4)

            ### Make the bot move

            #### Save last position in temp variables
            plx = px
            ply = py

            if dt == 1:        #### Direction 1 = Up
                py = py + 1
            elif dt == 2:      #### Direction 2 = Right
                px = px + 1
            elif dt == 3:      #### Direction 3 = Down
                py = py - 1
            elif dt == 4:      #### Direction 4 = Left
                px = px - 1

            if vi == True:
                ###Visual interpretation
                print(f"Iteration {i} - Move {j} - Direction {dt} - Bot pos {px}: {py}")

                for y in range(1, ly + 1):
                    for x in range(1, lx + 1):
                        if x == px and y == py:
                            print("0", end=" ")
                        elif x == plx and y == ply:
                            print("~", end=" ")
                        else:
                            print("*", end=" ")
                    print()
            ### Test if the bot has exited

            if px < 1 or py < 1 or px > lx or py > ly:
                cw[i] = j

                if vi == True:
                    print(f"Bot EXITED")
                break
        if vi == True:
            print()
    ## Results
    tEnd = t.time()
    results(r, n, cw, tStart, tEnd)


    ## Return to hub
    input("\nEnd. Sending back to Hub")
    return hub()





# Start

## Global variables and classes

vi = True   ### Toggles visual logging (WIP)

lx = 0      ### Grid length
ly = 0

stx = 0     ### Starting point
sty = 0

cw = {}     ### Number of moves to win only for each iteration c[i] = j

PRN = 2     ### Constant that define the precision of rounds in all the program

tStart = 0  ### Used for counting the execution time
tEnd = 0

## Run init()
init()

# Run functions for test


# Debug if program finished prematurely (the rescue loop)
while True:
    print("Warning - Program exited of the big loop")
    input("Press enter to go back to hub...")
    hub()