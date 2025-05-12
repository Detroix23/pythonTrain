# Imports
from random import *

"""
def sing():
    # Actual program

    ## Variables
    global lx, ly, stx, sty, cw, vi, tStart, tEnd

    r = 0  ### Iterations total
    n = 0  ### Number of maximum moves
    dt = 0  ### Random int between 1 and 4 that choose the direction of the bot (same probability to go to one of the 4 cardinal directons
    px = 0  ### Pos x of the bot
    py = 0  ### Pos y of the bot

    ## Setup parameters with the "grid()" function
    print("You will run the test. Please set the following paramters")
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


def run(r, n):
    ## External logging
    RESULTS.write(f"Single run with lx = {lx}; ly = {ly}, stx = {stx}; sty = {sty}\n")
    VI.write(f"Single run with lx = {lx}; ly = {ly}, stx = {stx}; sty = {sty}\n")

    print("The test will execute {} times, in a {} by {} grid where the bot start at {};{} and has a maximum of {} moves\n".format(r, lx, ly, stx, sty, n))

    ## Main loop

    ### Start timer
    tStart = t.time()

    for i in range(1, r + 1):
        px = stx
        py = sty
        for j in range(1, n + 1):
            dt = random.randint(1, 4)

            ### Make the bot move

            #### Save last position in temp variables
            plx = px
            ply = py

            if dt == 1:  #### Direction 1 = Up
                py = py + 1
            elif dt == 2:  #### Direction 2 = Right
                px = px + 1
            elif dt == 3:  #### Direction 3 = Down
                py = py - 1
            elif dt == 4:  #### Direction 4 = Left
                px = px - 1

            if vi == True:
                ###Visual interpretation
                print(f"Iteration {i} - Move {j} - Direction {dt} - Bot position {px}: {py}")

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
                    print("Bot EXITED")
                break
        if vi == True:
            print()
    ## Results
    tEnd = t.time()

    return results(r, n, cw, tStart, tEnd)
"""

def comb(L=4, MAX=1):
    #Variables
    u = []      ### N Try variables
    up = []     ### U prime
    h = []      ### History
    k = False   ### Flag True if u already exist

    # Init main variable
    for init in range(L):
        u.append(0)

    h.append(u)

    while len(h) < (L**(MAX+1)):

        k = False

        ri = randint(0, L-1)
        print("Ri taking new valor", ri)
        print("h1", h, end=" ")

        for v in range(MAX+1):
            up = u
            up[ri] = v
            print("h2", h, end=" ")

            for test in h:
                print(f"up: {up}, v: {v}, h: {h}, test: {test}", end=" ")
                if test == up:
                    print("h3", h, end=" ")
                    k = True
                    break

            print("h4", h, end=" ")
            if k == False:
                u = up
                h.append(u)
                print("h appended with", u)
                break
            else:
                print("k == True, no appends")
            print("h5", h, end=" ")


    return h



print(comb(2,1))





