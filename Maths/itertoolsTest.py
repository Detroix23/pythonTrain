# -*- coding: utf-8 -*-
"""
Test itertools
for M = 1 and L = 2 
[0, 1]
return [[0, 0], [0, 1], [1, 0], [1, 1]]
"""

import itertools as it

def run1(l=[]):
    
    for L in range(len(l)):
        for subset in it.combinations(l, L):
            print(subset)
    




def all_subsets(ss):
    return it.chain(*map(lambda x: it.combinations(ss, x), range(0, len(ss)+1)))

def run2(l):
    for subset in all_subsets(l):
        print(subset)
        


def run3(M, L):
    
    if M >= L:
        r = False
    
    else:
        m = []
        for v in range(M+1):
            m.append(v)
        
        q = L**(M+1)
        
        for a in range(M+1):
        
        
    
    
    

stuff = [0, 1, 2]


print(run2(stuff))