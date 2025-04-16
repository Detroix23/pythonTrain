import math
import turtle as tl

Ncote = 4
i = 1

for i in range(2):
    

    ## Aire du petit

    LcoteP = math.cos(math.radians(360/Ncote/2))
    print("LcoteP", LcoteP)

    print("Pythagore", (math.sqrt((1**2) - ((LcoteP/2)**2))))

    Ap = (Ncote * LcoteP) * (math.sqrt((1**2) - ((LcoteP/2)**2))/2)


    ## Aire du grand

    LcoteG = ((360/Ncote)/2 * math.tan(math.radians(1))) * 2

    # print(360/Ncote/2)
    # print(math.tan(math.radians(1)))

    print("Lcoteg", LcoteG)

    Ag = (Ncote * LcoteG) * (0.5)






    print("Ap", Ap)
    print("Ag", Ag)

    p = (Ag + Ap) / 2
    print("Iteration:", i)
    print("approx pi", p)

    
    Ncote = Ncote + 1
