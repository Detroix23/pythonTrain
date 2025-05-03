
"""
Find the most optimal circle placements in a square.
We'll simplify areas by doing a grid square; we'll round up.

"""
import math
import ccartesian as cc


M = True
l1, l2, l3 = [1,2,3], [1,2,3], [1,2,3]

class grid:
    """
    Class: Generate a grid. WIP
    """
    def __init__(self, xmax, ymax):
        self.grid = []
        for x in xmax:
            for y in ymax:
                self.grid.append([x, y])

                
class tile:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None
    
    def __str__(self):
        if self.name is not None:
            string = f"TILE - Name: {self.name}; Pos: x={self.x}, y={self.y}" 
        else:
            string = f"TILE - Pos: x={self.x}, y={self.y}" 
        
        return string
    
    def set_name(self, name):
        self.name = name
    
class vect:
    
    import math
    
    def __init__(self, x, y):
        self.name = None
        self.x = x
        self.y = y
    
    def __str__(self):
        if self.name is not None:
            string = f"TILE - Name: {self.name}; Pos: x={self.x}, y={self.y}" 
        else:
            string = f"TILE - Pos: x={self.x}, y={self.y}" 
        
        return string
    
    def set_name(self, name):
        self.name = name
        
    def mean(self):
        """
        Function: Give length of the vector
        """
        M = math.sqrt(self.x**2 + self.y**2)
        return M

class disk:
    
    SHAPE = "disk"
    
    def __init__(self, name, r=None, x=None, y=None):
        """
        Function: Create circle. Requieres at least a name.
        """
        self.name = name
        self.zone = None
        self.r = r
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"GEO - Name: {self.name}; Shape: {self.SHAPE}; Radius: {self.r}; Pos: x={self.x}, y={self.y}"
    
    def set_pos(self, x, y):
        """
        Function: Set position on virtual grid (0;x,y)
        """
        self.x = x
        self.y = y
    
    def set_radius(self, r):
        self.r = r
        
        
    def test_tile(self, x, y):
        if self.x is None or self.y is None:
            self.res = None
        
        # If variables are set, compare vectorial distance from shape.x, shape.y to x, y
        else:
            self.vect_test = vect(x - self.x, y - self.y)
            self.vect_test_len = self.vect_test.mean()
            
            if self.vect_test_len <= self.r:
                self.res = True
            
            else:
                self.res = False
        
        return self.res
    
    #End


class rectangle:
    SHAPE = "rectangle"

    def __init__(self, name, w=None, l=None, x=None, y=None):
        """
        Function: Create rectangle (or a square). Requires at least a name.
        """
        self.name = name
        self.zone = None
        self.l = l  ### X axis
        self.w = w  ### Y axis
        self.x = x
        self.y = y

    def __str__(self):
        return f"GEO - Name: {self.name}; Shape: {self.SHAPE}; Length: {self.l}; Width: {self.w}; Pos: x={self.x}, y={self.y}"

    def set_pos(self, x, y):
        """
        Function: Set position on virtual grid (0;x,y)
        """
        self.x = x
        self.y = y

    def set_size(self, l, w):
        self.l = l  ### X axis
        self.w = w  ### Y axis

    def test_tile(self, x, y):
        if self.x is None or self.y is None:
            self.res = None

        # If variables are set, if vectorial dimension are all lower than half of width and length, it's in.
        else:
            if abs(x - self.x) <= int(self.l/2) and abs(y - self.y) <= int(self.w/2):
                self.res = True
            else:
                self.res = False

        return self.res

    # End
    
def zone(shape, max_safe=-1):
    """
    Function: Generate all tiles of a shape, by testing in square spiral each tile. Starting from 0,0; going up then right.
    """
    x = shape.x
    y = shape.y
    i = 0
    fin = False
    compass = 0  ### 0: +y, 1: +x, 2: -y, 3: -x
    ## Init zone and do first test

    if shape.test_tile(x, y):
        zone = [(x, y)]
        zone_test = [(x, y)]
    else:
        zone = []
        zone_test = []
        
    while i < max_safe and not fin:
        #V1 Spiral
        """
        for move in range(i):
            x += 1
            if shape.test_tile(x, y):
                zone.append((x, y))

        ### Log movement
        print("ZONE - Tile checked:", (x, y))
        zone_test.append((x, y))
        print(zone_print(zone=zone_test, ymax=15, xmax=15, occ="# "))

        #print(f"ZONE - Iter: {i}, Pos testing: {x},{y}")
        
        for move in range(i): 
            y += 1
            if shape.test_tile(x, y):
                zone.append((x, y))

        ### Log movement
        print("ZONE - Tile checked:", (x, y))
        zone_test.append((x, y))
        print(zone_print(zone=zone_test, ymax=15, xmax=15, occ="# "))
        #print(f"ZONE - Pos testing: {x},{y}")
        """

        # V2 Spiral (no stop)

        ## Follow compass
        for l in range(int(i)):
            if compass == 0:
                y += 1
            elif compass == 1:
                x += 1
            elif compass == 2:
                y -= 1
            elif compass == 3:
                x -= 1

            ## Check tile
            if shape.test_tile(x, y) and (x,y) not in zone:
                zone.append((x, y))

            ### Log movement
            """
            print("ZONE - Tile checked:", (x, y), "for i =", i)
            zone_test.append((x, y))
            print(zone_print(zone=zone_test, xmin=-5, xmax=6, ymin=-5, ymax=6, occ="# ", org="° "))
            """

        ## Turn compass
        if compass < 3:
            compass += 1
        else:
            compass = 0




        i += 0.5
    return zone


def zone_print(zone, xmin=0, xmax=0, ymin=0, ymax=0, occ="# ", blk="* ", org=False, graduation=True):
    
    # Find min and max
    card = {
        "xmin": xmin,
        "xmax": xmax,
        "ymin": ymin,
        "ymax": ymax,
    }
    for tile in zone:
        ## Check min and max cardinals
        if tile[0] > card["xmax"]:
            card["xmax"] = tile[0]
        elif tile[0] < card["xmin"]:
            card["xmin"] = tile[0]
        if tile[1] > card["ymax"]:
            card["ymax"] = tile[1]
        elif tile[1] < card["ymin"]:
            card["ymin"] = tile[1]

    print("ZONE PRINT - Cardinals:", card)
    # Start plotting
    ## Vars
    ### Constants to fill spaces (2 character's optimal)
    OCC = occ
    BLK = blk
    ORG = org
    table = ""
    for x in range(card["xmin"], card["xmax"]+1, 1):
        for y in range(card["ymin"], card["ymax"]+1, 1):
            if org and (x, y) == (0, 0):
                table += ORG
            elif (x, y) in zone:
                table += OCC
            else:
                table += BLK
        ## New line
        table += "\n"

    x = card["xmin"]
    y = card["ymin"]
    while x < card["xmax"]+1:
        while y < card["ymax"]+1:
            if org and (x, y) == (0, 0):
                table += ORG
            elif (x, y) in zone:
                table += OCC
            else:
                table += BLK
            y += 1
        ## New line
        table += "\n"
        x += 1

    return table


d1 = disk("s1")
d1.set_radius(5)
d1.set_pos(2, 3)
print("SHAPE - Test disk 1: ", d1)

d1z = zone(d1, 16)
print("SHAPE - Test disk's 1 zone: ", d1z)

z1 = zone_print(zone=d1z, occ=" @ ", blk=" * ", org=" 0 ")
print("SHAPE - Zone 1:\n" + z1)


r1 = rectangle("r1")
r1.set_size(3,4)
r1.set_pos(2, 3)
print("SHAPE - Test rectangle 1: ", r1)

r1z = zone(r1, 255)
print("SHAPE - Test rectangle's 1 zone: ", r1z)

z2 = zone_print(zone=r1z, occ=" @ ", blk=" * ", org=" 0 ")
print("SHAPE - Rectangle's zone 1:\n" + z2)






















