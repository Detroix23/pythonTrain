from itertools import *

def ordin(R, S):
    

    R = str(R)
    LR = len(R)

    M = len(str(123*S))

    t = {}
    results = {}      ### Results dict

    laccept = []
    lsemi = []
    accept = []
    semi = []
    
    p = None

    # Definizione black list vuota
    for i in range(int(LR//3)):
        t[i] = []
    
    print("* Creazione ordine")            #### Debug
    # Definizione degli ordine

    qp = range(2, M+1)                      ## Liste larghezza prodotto
    qr = range(1, len(str(S))+1)        ## Liste larghezza random factor

    ## Ogni ordine degli prodotti
    pq = [r for r in product(qp, repeat=int(LR//3))]

    ## Ogni ordine degli rfactors
    pr = [r for r in product(qr, repeat=int(LR//3))]

    #print("pq, pr", pq, pr)

    ## Ogni ordine ((prodotti), (rfactors))
    print("* Uso ordine")
    for p1 in product(pq, pr):
        
        ### Sintesi nella forme ((prodotto, rfactor))
        p2 = []
        tq = p1[0]
        tr = p1[1]
        for i in range(len(tq)):
            p2.append((tq[i], tr[i]))
            
        #print("p2", p2, end=" - ")
        ### Eliminazione degli tuples ordinai con la longezza diff di R

        sm = 0
        for cpl in p2:
            for n in cpl:
                sm += n

        #### Prova di apiccolare p
        while sm > LR:
            p2.pop()
            sm = 0
            for cpl in p2:
                for n in cpl:
                    sm += n

        ### Elim degli tuples nella black list t {ind = [(),..]}
        cnt = 0
        ib = False
        while cnt < len(p2):
            for cpl in t[cnt]:
                if p2[cnt] == cpl:
                    ib = True
            cnt += 1

        #print("p2", p2, end=" - ")
        if ib or sm != LR:
            #print("p non valide", ib, sm)
            pass

        else:
            #print("p valide", end=" ")
            p = tuple(p2)
            # Uso degli ordine

            #print(f"div={int(LR/M)+1}, qp={qp}, qr={qr}, pq={1}, pr={2}, p1={p1}, p2={p2}, p={p}")
            #print(p, "P")
            ## Variables
            
            skip = 0
            dr = ""
            rr = ""

             ## Giri principale       
            ordr = p
            #print(f"\nTry {cont+1} with {ordr}:", end=" ")                 # Debug
            skip = 0
            tempr = []

            ### Va tra tutti i abbinamenti dell ordino
            cnt = 0
            while cnt < len(p):
                
                cpl = ordr[cnt]
                #### Prima larghezza, prodotto
                dr = ""
                for m in range(cpl[0]):
                    dr = dr + str(R[m + skip])

                dr = int(dr)
                skip += cpl[0]

                #### Seconda larghezza, rfactor
                rr = ""
                for m in range(cpl[1]):
                    rr = rr + str(R[m + skip])

                rr = int(rr)
                skip += cpl[1]
                
                #### Divisione + verifica dei fattori
                if rr == 0:
                    d = -1
                else:
                    d = dr / rr
                
                #print(f"(dr={dr}, rr={rr}, d={round(d, 1)})", end=" ")                     # Degug

               #### Puoi tratto della divisione 
                if d in range(97,123):
                    d = int(d)
                    #print(chr(d), end=" ")     # Debug
                    tempr.append(chr(d))

                elif type(d) == "float" or type(d) == "int":
                    tempr.append("/")
                    #print("/", end=" ")             # Debug

                    ##### Black list
                    black = t[cnt]
                    black.append(cpl)
                    t[cnt] = black
                    break
                    
                else:
                    tempr.append("#")
                    #print("#", end=" ")            # Debug

                    ##### Black list
                    black = t[cnt]
                    black.append(cpl)
                    t[cnt] = black
                    break


                cnt += 1

            tempr = tuple(tempr)
            print(tempr)    
            #results[ordr] = tempr
            #print("E:",results, ordr, tempr)

            ## Tratta tempr result
            if (not "/" in tempr) and (not "#" in tempr) and (tempr !=  ""):
                laccept.append(tempr)
            elif len(tempr) > 1:
                lsemi.append(tempr)

            ### Compacting resultati
            
            if laccept != []:
                for word in laccept:
                    tmpacc = ""
                    for letter in word:
                        tmpacc += letter
                    accept.append(tmpacc)

            if lsemi != []:
                for word in lsemi:
                    tmpacc = ""
                    for letter in word:
                        if letter != "/" and letter != "#":
                            tmpacc += letter
                    if not tmpacc in semi:
                        semi.append(tmpacc)
                              
    return accept, semi




# Inizzio dell Ui

print("* Lei usa la versione 0.30 dell decoder THe")


R = (input("Entra il codice a decodare (int): "))
try:
    R = int(R)
except ValueError:
    R = False

while R:                             ## Break quando l'user Enter
    print(f"Entrare i valore seguenti, R={R} (Enter to quit)")
    
    S = (input("Entra la larghezza massima dell random (default=9, int): "))
    try:
        S = int(S)
    except ValueError:
        break
    
    
    print(f"* Inizio del programma con S={S} & R={R}")

    accept, semi = ordin(R, S)

    print("\n\n* Resultati")
    
    if accept == "pv":
        print(" - Il programma è uscita in anticipo a causa di p stando vuoto")
    elif accept == "nr":
        print(" - Il programma sembra di avere trovato niente. Magari provare di aumentare S.")
        print(f"Risulatati incomplessi: {semi}")
    else:
        print(" - Il programma a trovato:\n{}".format(accept))


    input("\nPress Enter to continue...")
    
# 44046306 ni
