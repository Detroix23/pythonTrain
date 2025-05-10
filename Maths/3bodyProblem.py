"""
Simulation of planet movement
Use of gravitational formula: F = (m1*m2) / d**2
We consider that all elements are spherical
"""

# Imports
import math
## Representation
#import matplotlib.pyplot as plt
import pyxel

# Types
## type vect = tuple[float, float]

# Simulation
def mean(vect: list[float]) -> float:
    """
    Compute vector mean
    """
    return math.sqrt((vect[0]**2) + (vect[1]**2))

# GUI
class Board:
    def __init__(self, width: int = 128, height: int = 128, title: str = "Simulation", fps: int = 30,
                 edges: str = "none", mass_softener: float = 1000.0, gravitational_constant: float = (10**-11), exponent_softener: float = 0.0, bounce_factor: float = 1.0
                 ):
        """
        Initialize the game.
        Args:
            @edges (string): {none, hard, bounce, tor}
        """
        # Vars
        self.exponent_softener: float = exponent_softener    ### Distance expoential softener
        self.gravitational_constant: float = gravitational_constant
        self.mass_softener: float = mass_softener      ### Mass factor
        self.edges: str = edges
        self.width: int = width
        self.height: int = height
        self.title: str = title
        self.fps: int = fps
        self.bounce_factor: float = bounce_factor


        # Init elems
        ## Elems
        self.system: dict[str, Elem] = {
            "Plan1": Elem(self, 500, (445, 560), name="Plan1", size=5),
            "Plan2": Elem(self, 400, (440, 450), name="Plan2", size=4),
            "Plan3": Elem(self, 300, (425, 400), name="Plan3", size=3),
            "Plan4": Elem(self, 300, (400, 350), name="Plan4", size=6)
        }

        ## Representation
        ### Positions

        self.elemsX: list[float] = []
        self.elemsY: list[float] = []
        # print("## Initialization of the elements: ")
        for name, elem in self.system.items():
            self.elemsX.append(elem.position[0])
            self.elemsY.append(elem.position[1])
            # print("-", elem)

        # Init simulation screen
        pyxel.init(width=width, height=height, title=title, fps=fps)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        """
        Update simulation
        """
        # Calc interactions
        ## Check for each element, all elements.
        for elemMain in self.system.values():
            # print(elemMain.name, ":", elemMain.forceVector[0], elemMain.forceVector[1], end=" - ")
            for elemTarget in self.system.values():
                if elemMain != elemTarget:
                    target_force: tuple[float, float] = elemMain.gravitational_force_from(elemTarget)
                    elemMain.force_vector = (
                        elemMain.force_vector[0] + target_force[0],
                        elemMain.force_vector[1] + target_force[1])
        # print()
        # Move
        for elem in self.system.values():
            elem.move()

    def draw(self) -> None:
        """
        Draw all simulation
        """
        # Clear all
        pyxel.cls(0)
        # All elems
        for name, elem in self.system.items():
            elem.draw()


class Elem:
    """
    Define a stellar element
    """
    CHECK_RADIUS = 100
    
    def __init__(self, BOARD: Board, mass: int, position: tuple[float, float], force_vector: tuple[float, float] = (0, 0), velocity: float = 0,
                 color: int = 5, size: int = 2, name: str = ""
                 ) -> None:
        """
        Creation of the elem, with "mass, vInit, xStart, yStart, color=5, size=2".
        """
        self.BOARD: Board = BOARD
        self.mass: float = mass
        self.velocity: float = velocity
        self.position: tuple[float, float] = position
        self.force_vector: tuple[float, float] = force_vector

        self.size: int = size
        self.color: int = color
        self.name: str = name

    def __str__(self) -> str:
        return f"Elem {self.name} - Position: x={self.position[0]}; y={self.position[1]}, Mass: m={self.mass}, Force: x={self.force_vector[0]}; y={self.force_vector[1]}."

    def distance_to(self, target) -> float:
        """
        Compute distance between this elem and the target elem
        """
        return math.sqrt((self.position[0] - target.position[0]) ** 2 + (self.position[1] - target.position[1]) ** 2)
    
    def gravitational_force_from(self, target) -> tuple[float, float]:
        """
        Find the gravitational force vector
        """
        # Direction
        vector_distance: tuple[float, float] = (self.position[0] - target.position[0], self.position[1] - target.position[1])
        theta = math.atan2(vector_distance[1], vector_distance[0])          ### Radians
        ## theta_deg = math.degrees(theta)
        # Distance (limited)
        distance: float = self.distance_to(target)
        if distance < (self.size / 2 + target.size / 2):
            distance = (self.size / 2 + target.size / 2)
        # F force value
        force: float = (self.BOARD.gravitational_constant * self.mass * target.mass) / (distance ** (2 + self.BOARD.exponent_softener))
        # Force vector
        ### Rectification because we go anti-trigonometric way, clockwise.
        vector_force: tuple[float, float] = (force * -math.cos(theta), force * -math.sin(theta))

        return vector_force

    def does_collide_with(self, target) -> bool:
        ...
        return True

    def move(self) -> None:
        """
        Move the elem, according to force vector at a scale (mass) and checking collision
        """
        # Force
        self.position = (
            self.position[0] + (self.force_vector[0] / (self.mass * self.BOARD.mass_softener)),
            self.position[1] + (self.force_vector[1] / (self.mass * self.BOARD.mass_softener)))

        # Check edges
        ## New for version
        for axis1 in (0, 1):
            axis2: int = abs(axis1 - 1)
            force_vector_list: list[float] = list(self.force_vector)

            if self.position[axis1] + self.size / 2 >= self.BOARD.width or self.position[axis1] <= 0:
                if self.BOARD.edges == "bounce":
                    force_vector_list[axis1] = self.force_vector[axis1] * -self.BOARD.bounce_factor
                    force_vector_list[axis2] = self.force_vector[axis2]

                elif self.BOARD.edges == "hard":
                    force_vector_list[axis1] = 0.0
                    force_vector_list[axis2] = self.force_vector[axis2]

            self.force_vector = (force_vector_list[0], force_vector_list[1])

    def draw(self) -> None:
        """
        Draw itself on the board
        """
        size2 = self.size / 2
        pyxel.rect(self.position[0] - size2, self.position[1] - size2, self.size, self.size, col=self.color)
        pyxel.rect(self.position[0], self.position[1], 1, 1, col=self.color + 1)



# Run
print("# Three body problem simulations")
# Completion
SIM: Board = Board(width=1000, height=1000, title="Simulation", fps=30, edges="bounce",
                   mass_softener=100, gravitational_constant=(6.67*(10**1)), exponent_softener=-0.3, bounce_factor=0.9)

print("---\nEnd")




