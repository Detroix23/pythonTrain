"""
Part of the enconding series
For each letter, take the key and shift it every time
"""


def uniAl(uniMin, uniMax):
    al = {}
    for code in range(uniMin, uniMax):
        al[chr(code)] = code;
    return al
    
def restrictLoop(val, limMin, limMax):
    d = limMax - limMin
    if d <= 0:
        r = False
    else:
        while val > limMax:
            val = val - d;
        while val < limMin:
            val = val + d;
        
        r = val;
        
    return r
    


        
def keyAdd(value, key, separtor="", uniMin=97, uniMax=123):
    """
    Pre: For now, need to be lowercase alphabetical
    """    
    enAr = [];
        
    al = uniAl(uniMin, uniMax);
    
    for charVal in value:
        if charVal in al.keys():
            
            keyShifted = ""
            for charKey in key:
                shiftCode = restrictLoop(al[charKey] + al[charVal], uniMin, uniMax)
                keyShifted = keyShifted + chr(shiftCode)
            
            enAr.append(keyShifted)
            
        else:
            enAr.append(" ")
    
    en = separtor.join(enAr)
    
    return en
    

val = "coucou la terre"
key = "abc "
valEn = keyAdd(val, key, "")
print("Encoded:",valEn)

