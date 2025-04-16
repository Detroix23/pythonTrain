#START
#import matplotlib.pyplot as plt

#Deprecated class thingy for the logs
class logs:
    #General logs
    ##i for iteration, fun for which function, r for result
    def __int__(self, i, fun, r):
        self.i = i
        self.fun = fun
        self.r = r

    def __str__(self):
        return f"\n{self.i}: {self.fun} -> {self.r}"

#Reverse fibo allow to find by which number n is surrounded in the  Fibonacci suite
def ff():
    global log, cl, p, git

    #User input
    while True:
        print("Please input an integer to be tested in the Fibonacci suite")
        z = input()
        try:
            z = int(z)
            if z < 1:
                print("Warning - Invalid input, must be above zero. Please try again")
            else:
                break

        except ValueError:
            print("Warning - Invalid input, not an integer. Please try again")

    #Variables

    c = 0  ##Counter (cannot start at 1)
    u = 0  ##2nd number
    t = 1  ##1st number
    l = []

    #Loop
    while u <= z:
        t = t + u
        u = t - u
        l.append(u)
        c = c + 1



    #Results
    if z == l[c-2]:
        print("{} is in the Fibonacci Suite, surrounded like this:".format(z))
        print(l[c - 3], l[c - 2], l[c - 1])
        ## Logs true (add directly formated in the form "iteration", "Function type", "Output")
        templ = ["\n", git, "Fibonacci", [l[c - 3], l[c - 2], l[c - 1]]]
        glogs.append(templ)
    else:
        print("{} is not in the Fibonacci Suite, but it's located between these two number of the suite:".format(z))
        print(l[c - 2],l[c - 1])
        ## Logs false
        templ = ["\n", git, "Fibonacci", [l[c - 2], z, l[c - 1]]]
        glogs.append(templ)

    ##Detailed results
    if p == True:
        print("Print complete generated list of Fibonacci suite:\n", l)
        #plt.plot(l, c)


    #Exit + iteration
    templ = []
    git = git + 1
    return hub()

def gar1():
    #GARLATTI SUITE Num1, this is a suite where a, b, c, d (following each other in the suite) respect (b*c)/a = d. It start with 1, 2, 3.
                                                                                    #Dividing by a allow to weight down the result


    #init
    global git, glogs
    ##Variables
    g = 1
    h = 2
    i = 3
    j = 0

    l = [1, 2, 3] ###Result list of this suite
    c = 3  ###Internal iteration counter (start at 1 higher incrementation would allow less operation when counting in the list below, but exceed list index (?))
           ###Here it start at 3 because of the number of variable ig
    #User input
    while True:
        print("Please input an integer to be tested in the Garlatti suite")
        z = input()
        try:
            z = int(z)
            if z < 4:
                print("Warning - Invalid input, must be above three. Please try again")
            else:
                break

        except ValueError:
            print("Warning - Invalid input, not an integer. Please try again")
    #Loop
    while j < z:
        ##Base calcul & save result
        j = (h*i)/g
        l.append(j)

        ##Offset all variables
        g = h
        h = i
        i = j
        c = c + 1

    #Results
    if z == l[c-1]:
        print("{} is in the Garlatti Suite N1, surrounded like this:".format(z))
        print(l[c - 3], l[c - 2], l[c - 1])
        ## Logs true (add directly formated in the form "iteration", "Function type", "Output")
        templ = [git, "Garlatti n1", [l[c - 3], l[c - 2], l[c - 1]]]
        glogs.append(templ)
    else:
        print("{} is not in the Garlatti Suite n1, but it's located between these two number of the suite:".format(z))
        print(l[c-2], l[c-1])
        ## Logs false
        templ = [git, "Garlatti n1", [l[c - 2], z, l[c - 1]]]
        glogs.append(templ)


    #Detailled results
    if p == True:
        print("Print complete generated list of Garlatti suite n1:\n", l)
        #plt.plot(l, c)



    # Exit + iteration
    templ = []
    git = git + 1
    return hub()



def hub():
    global p
    while True:
        print("HUB\n'l' for logs, 'p' to print, 'f' to start Fibonacci, '1' to start garlatti 1")
        h = str(input())
        if h == "p":
            if p == True:
                p = False
                print("Print off")
            else:
                p = True
                print("Print on")
        elif h == "l":
            return printlogs()
        elif h == "f":
            return ff()
        elif h == "1":
            return gar1()
        else:
            print("Warning - Invalid input. Please try again")

def printlogs():
    print('Global logs', *glogs, sep='\n- ')
    return hub()

#Init
##Global variables

glogs = []    ##Global logs history
git = 0       ##Global iterations
p = False     ##Boolean that determine if print is enabled

##Start
hub()