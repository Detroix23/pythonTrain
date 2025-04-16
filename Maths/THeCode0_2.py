
"""
Encodeur d'une entrée par des nombres aléatoires,
Idée de Thiago, ou l'output serait une suite de nombre: "nnnnrnnnrnnnnr"

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
    p = 0
    pr = ""      ### Presumably r
    S = input("Randomness size excpetced")
    
    while True:
        
        while p <= 2 * len(R):                  ### Advance all the loops
            
            for n in range(2,len(str(123*S))):  ### Loop for all possible r lengths
                for som in range(n):            ### Take the n caracter number
                    pr = pr + R[som + p * n]
                pr = int(pr)
                for interval in range(97,123):  ### Check if that number correspond to real letter
                    if interval == pr:
                        print(chr(pr))          ### Return smthing if letter
            p = p + 1
                    
    
    
    

            

while True:
    R = inp()
    
    print("Encoded:", R)
    