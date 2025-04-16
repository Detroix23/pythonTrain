
"""
Visualier le nombre de multiple qu'a un nombre x
"""
#Imports
import matplotlib.pyplot as plt


#Gobal variables

##Images y
nm = []
##Antecedants x
xx = []
#Variable style of the line
gr = ""

def muls(debug=None):
    #Variables
    c = 0
    global nm
    global xx
    global gr
    
    r = int(input("Limite d'iterations pour tout les diviseurs: "))
    for n in range(2,r+1):
        c = 0
        print("\n{}".format(n), end="- ")
        for m in range(1, n+1):
            ## Generer diviseurs
            if n%m==0:
                ## Afficher
                print(m, end=" ")
                
                c = c + 1
        ##Engergistrer
        nm.append(c)
        
        #print("c=", c,end="")
        
        ##Creer l'axe x
        xx.append(n)
    
    ##Retour d'info supplementaires
    gr = "-"
    return graph()



def prem(debug=None):
    
    #Fonction qui sert a calculer chaque nombre premier
    
    #Variables
    global nm
    global xx
    global gr
    
    nm = [0,0,2]
    xx = [0,1,2]
    
    r = int(input("Limite d'iterations pour tout le nombres premiers: "))
    for n in range(3,r+1):
        c = 0
        print("\n{}".format(n), end="- ")
        for m in range(2,n):
            ## Generer diviseurs
            if n%m==0:
                ## Afficher
                print(m, end=" ")     
                c = c + 1
            elif c > 0:
                break
        
        if c == 0:
            nm.append(n)

            xx.append(n)
        
        if debug==True:
            print("Debug nm, c ", nm, c)
            
    gr = "ro"
    return graph()


def graph():
    global xx
    global nm
    global gr
    
    plt.plot(xx, nm, gr)
    plt.ylabel('y')
    plt.xlabel("x")
    plt.show()

prem(True)
            