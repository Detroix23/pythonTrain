"""
Simulation of planet movement
Use of gravitational formula: F = (m1*m2) / d**2
We consider that all elements are spherical
"""
# Imports
import math
## Representation
import matplotlib.pyplot as plt
import pyxel

# Simulation
def mean(vect):
    """
    Compute vector mean
    """
    return math.sqrt((vect[0]**2) + (vect[1]**2))

class Elem:
    """
    Define a stellar element
    """
    CHECK_RADIUS = 100
    
    def __init__(self, BOARD, mass, xStart, yStart, fInit=[0, 0], vInit=0, color=5, size=2, name=""):
        """
        Creation of the elem, with "mass, vInit, xStart, yStart, color=5, size=2".
        """
        self.B = BOARD
        self.mass = mass
        self.velocity = vInit
        self.pos = [xStart, yStart]
        self.forceVector = fInit

        self.size = size
        self.color = color
        self.name = name

    def __str__(self):
        return f"Elem {self.name} - Position: x={self.pos[0]}; y={self.pos[1]}, Mass: m={self.mass}, Force: x={self.forceVector[0]}; y={self.forceVector[1]}."

    def distance_to(self, target):
        """
        Compute distance between this elem and the target elem
        """
        return math.sqrt((self.pos[0] - target.pos[0])**2 + (self.pos[1] - target.pos[1])**2)
    
    def gforce_from(self, target):
        """
        Find the gravitational force vector
        """
        # Direction
        vectorDistance = [self.pos[0] - target.pos[0], self.pos[1] - target.pos[1]]
        # print(vectorDistance[1] / vectorDistance[0], vectorDistance[1], vectorDistance[0])
        theta = math.atan2(vectorDistance[1], vectorDistance[0])    ### Radians
        ## thetaDeg = math.degrees(theta)
        # Distance (limited)
        r = self.distance_to(target)
        if r < (self.size / 2 + target.size / 2):
            r = (self.size / 2 + target.size / 2)
        # Value
        F = (self.B.G * self.mass * target.mass) / (r ** (2 + self.B.ra))
        # Force vector
        ### Rectification because we go anti-trigonometric way, clockwise.
        vectorForce = [F * -math.cos(theta), F * -math.sin(theta)]

        # if F > 0.1:
            # print("Interaction:", F)
            # print("Force vector:", vectorForce)
        return vectorForce

    def collision_with(self, target):
        pass

    def move(self):
        """
        Move the elem, according to force vector at a scale (mass) and checking collison
        """
        # Force
        self.pos = [
            self.pos[0] + (self.forceVector[0] / (self.mass * self.B.d)),
            self.pos[1] + (self.forceVector[1] / (self.mass * self.B.d))]

        # Check edges
        if self.pos[0] + self.size / 2 > self.B.width:
            if self.B.edges == "bounce":
                self.forceVector = [
                    self.forceVector[0] * -self.B.bounceFactor,
                    self.forceVector[1]]
            elif self.B.edges == "hard":
                self.forceVector = [
                    0,
                    self.forceVector[1]]
        elif self.pos[0] < 0:
            if self.B.edges == "bounce":
                self.forceVector = [
                    self.forceVector[0] * -self.B.bounceFactor,
                    self.forceVector[1]]
            elif self.B.edges == "hard":
                self.forceVector = [
                    0,
                    self.forceVector[1]]
        if self.pos[1] + self.size / 2 > self.B.height:
            if self.B.edges == "bounce":
                self.forceVector = [
                    self.forceVector[0],
                    self.forceVector[1] * -self.B.bounceFactor]
            elif self.B.edges == "hard":
                self.forceVector = [
                    0,
                    self.forceVector[1]]
        elif self.pos[1] < 0:
            if self.B.edges == "bounce":
                self.forceVector = [
                    self.forceVector[0],
                    self.forceVector[1] * -self.B.bounceFactor]
            elif self.B.edges == "hard":
                self.forceVector = [
                    0,
                    self.forceVector[1]]


    def draw(self):
        """
        Draw itself on the board
        """
        s2 = self.size / 2
        pyxel.rect(self.pos[0] - s2, self.pos[1] - s2, self.size, self.size, col=self.color)
        pyxel.rect(self.pos[0], self.pos[1], 1, 1, col=self.color+1)

# GUI
class Board:
    def __init__(self, width=128, height=128, title="Simulation", fps=30, edges="none", d=1000.0, G=(10**-11), ra=0.0, bounceFactor=1.0):
        """
        Initialize the game.
        Args:
            @edges (string): {none, hard, bounce, tor}
        """
        # Vars
        self.ra = ra    ### R expoential arrengement, softener
        self.G = G
        self.d = d      ### D factor
        self.edges = edges
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.bounceFactor = bounceFactor


        # Init elems
        ## Elems
        self.system = {
            "Plan1": Elem(self, 500, 445, 560, name="Plan1", fInit=[-10000, 0], size=5),
            "Plan2": Elem(self, 400, 440, 450, name="Plan2", fInit=[10000, 0], size=4),
            "Plan3": Elem(self, 300, 425, 400, name="Plan3", fInit=[-5000, 5000], size=3),
            "Plan4": Elem(self, 300, 400, 350, name="Plan4", fInit=[-2000, 3000], size=6)
        }

        ## Representation
        ### Positions

        self.elemsX = []
        self.elemsY = []
        # print("## Initialization of the elements: ")
        for name, elem in self.system.items():
            self.elemsX.append(elem.pos[0])
            self.elemsY.append(elem.pos[1])
            # print("-", elem)

        # Init simulation screen
        pyxel.init(width=width, height=height, title=title, fps=fps)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):
        """
        Update simulation
        """
        # Calc interactions
        ## Check for each element, all elements.
        for elemMain in self.system.values():
            # print(elemMain.name, ":", elemMain.forceVector[0], elemMain.forceVector[1], end=" - ")
            for elemTarget in self.system.values():
                if elemMain != elemTarget:
                    targetForce = elemMain.gforce_from(elemTarget)
                    elemMain.forceVector = [
                        elemMain.forceVector[0] + targetForce[0],
                        elemMain.forceVector[1] + targetForce[1]]
        # print()
        # Move
        for elem in self.system.values():
            elem.move()

    def draw(self):
        """
        Draw all simulation
        """
        # Clear all
        pyxel.cls(0)
        # All elems
        for name, elem in self.system.items():
            elem.draw()


# Run
print("# Three body problem simulations")
# Completion
SIM = Board(width=1000, height=1000, title="Simulation", fps=30, edges="bounce", d=100, G=(6.67*(10**1)), ra=-0.3, bounceFactor=0.9)





