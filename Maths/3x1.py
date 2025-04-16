#Ininit

import os

##Logs of all results
### It is indexed "starting number": "number of iterations"
logR = {}

c = 0
def it(U):
    #Variables
    n = U
    i = 0
    logI = []

    #Output logs ?
    print('Logs = Y or N')
    Ylog = input()
    if not Ylog == "Y" or Ylog == "N":
        print("Error - Incorrect input")
        return hub()


    #Computing 3*x+1
    while n!=1:
        i = i + 1
        print("Computing the number of iterations needed to reach 1 for ",U)
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        print("Actual  number = ",n, " ____ Iterations = ",i)
        os.system("cls")
        logI.append(n)

    #Results
    print("It took",i,"iterations for the number",U,"to reach 1")

    #Logs

    ##Iterations logs
    if Ylog == 'Y':
        print(logI)
    return hub()

    ##Results logs
    logR[U] = i


def hub():
    #Type the number and the following action will be executed
    print("Action:\n1 - Test number\n2 - Output general logs\n")
    c = input()

    if c == 0:
        return hub()

    elif c == 1:
        print("Enter an integer as the starting point of the script")
        it = input()
        return it(int(it))

    elif c == 2:
        print("Outputting all general logs")
        print(logR)
        return hub()

    else:
        return hub()



def comp():
    print("uwu")

hub()

print("Error - Program reached end")