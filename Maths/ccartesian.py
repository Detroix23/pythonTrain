
"""
Fiddling with cartesian products to replace and optimize itertools'

"""

def repeat(n, l):
    """
    Function: Puts in a list n time a given list
    """
    return [l for i in range(n)]


def cart_product_1(M, *seqs):
    """
    Function : Custom cartesian products function w/ inline loops
    Args:
        - M int or bool: define the sum required the list to be. Set to False to ignore
        - seqs iterable: many list that you want
        
    """
        
    if not seqs:
        return [[]]
    else:
        return [[x] + p for x in seqs[0] for p in cart_product_1(M, *seqs[1:])]



def cproduct(M, *seqs):
    """
    Function : Custom cartesian products function with blocks loops
    Args:
        - M int or bool: define the sum required the list to be. Set to False to ignore
        - seqs iterable: many list that you want
    """       
    r = []
    if seqs:
        for x in seqs[0]:
            for p in cart_product_1(M, *seqs[1:]):
                #Debug  print(f"x={x} p={p}")
                rt = tuple([x] + p)
                if M == True or sum(rt) == M:
                    r.append(rt)
                rt = []
    
    return r

def cyield(M, *seqs):
    """
    Function : Custom cartesian products function with blocks loops
    Args:
        - M int or bool: define the sum required the list to be. Set to False to ignore
        - seqs iterable: many list that you want
    """       
    r = []
    if seqs:
        for x in seqs[0]:
            for p in cart_product_1(M, *seqs[1:]):
                #Debug print(f"x={x} p={p}")
                rt = tuple([x] + p)
                if M == True or sum(rt) == M:
                    yield rt
                rt = []
    
    return

"""
M = 5
l = []
print(f"================================\nResults M={M}:")
print(cproduct(M, l))
M = 5
l1, l2, l3 = [1,2,3], [1,2,3], [1,2,3]
print(f"================================\nResults M={M}:")
print(cproduct(M, l1, l2, l3))
M = 5
l1, l2, l3 = [1,2,3], [1,2,3], [1,2,3]
print(f"================================\nResults M={M}:")
print(cproduct(M, l))
"""


def backpack_brut(items, w, p):
    """
    Function: The back pack problem, P == NP ?
    Args:
        items (dict): list of items {item: {weight: 54, price: 54}}
        
    """
    pass


















