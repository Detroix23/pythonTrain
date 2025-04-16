
"""
Encodeur d'une entrée par des nombres aléatoires,
Idée de Thiago, ou l'output serait une suite de nombre: "00001111"

* Algo de codage: val * nb aleatoire - fibo(n)  
* Cracking algo: 
"""


from random import *


def al(style="lil"):
    #Create the alphabet dict L[code] = "letter"
    print("* Creating alphabet")
    
    L = {}
    
    if style == "lil":
        for code in range(97,123):
            val = str(code)
            """
            while len(val) < 4:
                val = "0" + val
            """
            
            #print(val,code,chr(code))          ### Debug
            L[code] = str(chr(code))
    return L

def inp():
    #Ask user
    print("\n* Start encoder")
    c = input("Type text to encode: ")
    c = c.lower()
    
    S = input("Size of randomness (int): ")
    S = int(S)
    
    rch = enc(c, S)
    
    return rch


def enc(c, S):
    
    print("* Starting the encoding process")
   
    # Variables
    L = al()    #Alphabet
    fiboa = 1
    fibob = 1
    rt = {}     #Results in a nice dict
    rch = ""    #Results on 1 line
    
    #Enumerate letters
    for lc in c:
        
        r = -1
        
        for code, ll in L.items():              ### Watch out! Evil break
            if lc == " ":
                r = 0
            elif lc == ll:
                
                #Encode
                ## Random value
                ranv = randint(1, S)
                fiboa = fiboa + fibob
                
                r = code * ranv - fiboa
                
                rt[r] = ranv
                print(code,ranv,fiboa,r)       ### Debug
        if r == -1:
            #If not in alphabet
            rt[lc] = ""
            
            print(lc)                          ### Debug
    
    #Loop dict to set all the chars on one line 

    
    for a, b in rt.items():
        rch = rch + str(a) + str(b)
        
    return rch
            

def decod(R):
    
    pr = 0      ### Presumably r
    S = input("Randomness size excpetced")
    
    while True:
        for i in range(1,len(str(S))+1):        ### Try for diff S
            
            for n in range(2,len(str(S))+2):      ### Try for sums ranging from 2ch and 
                for som in range(n):
                    pr = pr + int(R[som])
                if int(pr/(n+1)):
                    pass
        
    
    
    

            

while True:
    R = inp()
    
    print("Encoded:", R)
    