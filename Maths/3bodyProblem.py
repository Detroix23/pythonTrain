# Simulation of planet movement
## Use of gravitational formula: F = (m1*m2) / d**2
import math
import matplotlib.pyplot as plt

global P
P = 3
global G
G = 6.67 * (10 ** -11)

# Vars
class Elem:
    """
    Define a stellar element
    """
    CHECK_RADIUS = 100
    
    def __init__(self, mass, vInit, xStart, yStart):
        self.mass = mass
        self.velocity = vInit
        self.pos = [xStart, yStart]
        self.force = [0, 0]
        
    def distance_to(self, target):
        """
        Compute distance between this elem and the target elem
        """
        return math.sqrt((self.pos[0] - target.pos[0])**2 + (self.pos[1] - target.pos[1])**2)
    
    def force_from(self, target):
        """
        Find the gravitational force vector
        """
        # Direction
        vectorDistance = [self.pos[0] - target.pos[0], self.pos[1] - target.pos[1]]
        theta = math.asin(vectorDistance[1] / vectorDistance[0])
        thetaDeg = math.degrees(theta)
        # Value
        F = (self.mass * target.mass) / (self.distance_to(target) ** 2)
        
        return thetaDeg


# Run
## Elems
system = {
    "Plan1" : Elem(50, 0, 10, 5),
    "Plan2" : Elem(40, 0, 0, 0)
}

print(system["Plan1"].force_from(system["Plan2"]))
## Representation
### Positions
elemsX = []
elemsY = []
for name, elem in system.items():
    elemsX.append(elem.pos[0])
    elemsY.append(elem.pos[1])

plt.plot(elemsX, elemsY, 'ro')
plt.show()











