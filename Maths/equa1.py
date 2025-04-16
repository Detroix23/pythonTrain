

"""
Solve equations in Python
V1 on the 09/01/2025

Imports
"""
from math import *


class solve:
    
    def second(a, b=0, c=0, OUT=("s")):
        """
        Function : Solve second degree polynomial 
        
        Args :
        [float] a : Degree 2nd, float, shall not be 0
        [float] b : Dergee 1st, float, optional (default 0)
        [float] c : Constant, float, optional (default 0)
        [tuple] OUT : Descrive what info should be returned; shall, only in lowercase, disregarding order, contain "s" for solutions, "delta" for delta. Tuple.

        Returns :
        [tuple] r
        Contains results according OUT specifications

        """
        # Vars
        if (b != ""):
            b = float(b)
        else:
            b = 0
        if (c != ""):
            c = float(c)
        else:
            c = 0
        r = []
        
        # Verif
        if ((a == 0) or (a == "") or (not "a" in locals())):
            s = (False)
            delta = False
            r = (False)
        
        else:
            a = float(a)
            
            # Main
            delta = b**2 + 4 * a * c
            
            if delta > 0:
                x1 = (-b - sqrt(delta) / 2*a)
                x2 = (-b + sqrt(delta) / 2*a)
                s = (x1, x2)
            elif delta < 0:
                s = (None)
            else:
                x0 = (-b / 2*a)
                s = (x0,)
            
            for data in OUT:
                if data == "s":
                    r.append(s)
                elif data == "delta":
                    r.append(delta)
            
            r = tuple(r)
            
        return r
    
    def first(a, b, OUT="s"):
        """
        Function : Solve first degree polynomial 
        
        Args :
        [float] a : Dergee 1st, float, shall not be 0
        [float] b : Constant, float, optional (default 0)
        [tuple] OUT : Descrive what info should be returned; shall, only in lowercase, disregarding order, contain "". WIP. Tuple.

        Returns :
        [tuple] r
        Contains results according OUT specifications

        """
        # Vars
        r = []
        if (b != ""):
            b = float(b)
        else:
            b = 0
        r = []
        
        # Verif
        if ((a == 0) or (a == "") or (not "a" in locals())):
            s = (False)
            delta = False
            r = (False)
        else:
            a = float(a)
            
            # Main
            x = -b / a
            
            # Results          
            for data in OUT:
                if data == "s":
                    r.append(x)
            
            r = tuple(r)
            
            return r
        


def precisionFloat(T):
    """
    Function: Test limits of float precision, decimal wise
    Args: 
    @ [int] T, number to be tested
    """
    equ = False
    T = 0
    i = 0
    di = T + 1
    
    while not equ and i <= 100:
        print(f"Iteration: {i}, Testing: {T}, Tester: {di}")
        if di == T:
            equ = True
            
        i = i + 1
        di = 10**-i
    
    return di


# UI

print("\nTest - 1.1 - Solving a second degree polynomial")
aIn = 5
bIn = 4
cIn = 4
print(f"a = {aIn}, b = {bIn}, c = {cIn}")
print(solve.second(aIn, bIn, cIn, ("s", "delta")))

print("\nTest - 2.1 Solving a first degree polynomial")
aIn = 5
bIn = 4
print(f"a = {aIn}, b = {bIn}")
print(solve.first(aIn, bIn))