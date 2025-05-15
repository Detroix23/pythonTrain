"""
Simulation of planet movement
Use of gravitational formula: F = (m1*m2) / d**2
We consider that all elements are spherical
"""

# Imports
import math
import random
## Representation
#import matplotlib.pyplot as plt
import pyxel

# Types
## type vect = tuple[float, float]

# Simulation
def listing_input(text: str, allowed: str = 'int') -> str:
    listening: list[str] = ['q', 'quit']
    input_result = input(text)
    for i in range(1, len(listening)):
        if input_result.strip().lower() == listening[i]:
            raise ValueError('Exit')
    try:
        if allowed == 'str':
            str(input_result)
        elif allowed == 'int':
            int(input_result)
    except Exception:
        raise

    return input_result
def mean(vect: list[float]) -> float:
    """
    Compute vector mean
    """
    return math.sqrt((vect[0]**2) + (vect[1]**2))

# GUI
class Board:
    def __init__(self, system: dict[str, tuple], width: int = 128, height: int = 128, title: str = "Simulation", fps: int = 30,
                 edges: str = "none", mass_softener: float = 1000.0,
                 gravitational_constant: float = (10**-11), exponent_softener: float = 0.0, bounce_factor: float = 1.0,
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
        self.time_speed: float = 0
        self.time_speed_previous: float = 1

        # Text
        self.texts_main: list[str] = [""]

        # Debug
        self.first_update = True

        # Init elements
        ## Elements
        self.system: dict[str, Elem] = {}
        
        for element_name, element_stats in system.items():
            self.system[element_name] = Elem(self, 
                                             mass=element_stats[0],
                                             position=element_stats[1],
                                             name=element_stats[2],
                                             size=element_stats[3]
                                             )
        
        
        
        print("- Provided system: ")
        print(system)
        print("- Saved system: ")
        print(self.system)
        
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
        print("- Pyxel board initialized")
        
        # Run
        pyxel.run(self.update, self.draw)
        print("# Game ended")

    def user_inputs(self) -> None:
        """
        Listen to user inputs
        """
        if pyxel.btn(pyxel.KEY_SPACE) and self.time_speed != 0:
            self.time_speed_previous = self.time_speed
            self.time_speed = 0
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.time_speed = self.time_speed_previous

        elif pyxel.btn(pyxel.KEY_1):
            self.time_speed = 0.1
        elif pyxel.btn(pyxel.KEY_2):
            self.time_speed = 0.5
        elif pyxel.btn(pyxel.KEY_3):
            self.time_speed = 1
        elif pyxel.btn(pyxel.KEY_4):
            self.time_speed = 2
        elif pyxel.btn(pyxel.KEY_5):
            self.time_speed = 4
        elif pyxel.btn(pyxel.KEY_6):
            self.time_speed = 10

    def text_main(self, text_color: int = 8) -> None:
        x = y = 10
        self.texts_main = [
            "# Three Body Problem - title=" + self.title + "; edges=" + self.edges + ", fps=" + str(self.fps) + ", frames=" + str(pyxel.frame_count),
            "- Elements: total=" + str(len(self.system)) + "",
            "- Time: speed=" + str(self.time_speed) + "",
            "---"]
        for txt in self.texts_main:
            pyxel.text(x, y, txt, text_color)
            y += 6

    def update(self) -> None:
        """
        Update simulation
        """
        # Debug
        if self.first_update:
            print("- Game running")
            self.first_update = not self.first_update
        # Inputs
        self.user_inputs()

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

        # Text
        self.text_main()

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
    
    def __repr__(self) -> str:
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
            self.position[0] + (self.force_vector[0] / (self.mass * self.BOARD.mass_softener) * self.BOARD.time_speed),
            self.position[1] + (self.force_vector[1] / (self.mass * self.BOARD.mass_softener) * self.BOARD.time_speed)
        )

        # Check edges
        ## New for version
        for axis1 in (0, 1):
            axis2: int = abs(axis1 - 1)
            force_vector_list: list[float] = list(self.force_vector)
            position_list: list[float] = list(self.position)

            if self.position[axis1] + self.size / 2 >= self.BOARD.width:
                if self.BOARD.edges == "bounce":
                    force_vector_list[axis1] = self.force_vector[axis1] * -self.BOARD.bounce_factor
                    force_vector_list[axis2] = self.force_vector[axis2]
                    ### Force it to be in the board and count reflexion
                    position_list[axis1] = 2 * self.BOARD.width - self.size / 2 - self.position[axis1]

                elif self.BOARD.edges == "hard":
                    force_vector_list[axis1] = 0.0
                    force_vector_list[axis2] = self.force_vector[axis2]
                    ### Force it to be in the board
                    position_list[axis1] = self.BOARD.width - self.size / 2
                    
            elif self.position[axis1] <= 0:
                if self.BOARD.edges == "bounce":
                    force_vector_list[axis1] = self.force_vector[axis1] * -self.BOARD.bounce_factor
                    force_vector_list[axis2] = self.force_vector[axis2]
                    ### Force it to be in the board and count reflexion
                    position_list[axis1] = 0

                elif self.BOARD.edges == "hard":
                    force_vector_list[axis1] = 0.0
                    force_vector_list[axis2] = self.force_vector[axis2]
                    ### Force it to be in the board
                    position_list[axis1] = 0


            self.force_vector = (force_vector_list[0], force_vector_list[1])
            self.position = (position_list[0], position_list[1])

    def draw(self) -> None:
        """
        Draw itself on the board
        """
        size2 = self.size / 2
        pyxel.rect(self.position[0] - size2, self.position[1] - size2, self.size, self.size, col=self.color)
        pyxel.rect(self.position[0], self.position[1], 1, 1, col=self.color + 1)



# Run
print("# Three body problem simulations")
## Config
user_mode: str = input("Please select a mode {rand/conf/default}[default]: ")
system_input: dict[str, tuple[int, tuple[int, int], str, int]] = {}


if user_mode not in ["", "rand", "conf", "default"]:
    user_mode = "default"
    print("(!) - Incorrect input; set to 'default'")
    

if user_mode == "rand":
    print("# Mode selected: rand (random generation)")
    number_elements: int = random.randint(3, 5)
    i: int = 1
    while i <= number_elements:
        name_random: str = "Plan" + str(i)
        mass_random: int = random.randint(200, 800)
        position_x_random = random.randint(400, 600)
        position_y_random = random.randint(400, 600)
        system_input[name_random] = (mass_random, (position_x_random, position_y_random), name_random, int(mass_random / 100))
        i += 1

elif user_mode == "conf":
    user_exit: bool = False
    print("# Mode selected: conf (manual configuration);")
    while not user_exit:
        if system_input: print("Currently loaded: ")
        for element in system_input:
            print("- " + element)

        print("New element: respect type, 'q' to validate to launch")
        manual: dict[str, str] = {}
        try:
            manual['name'] = listing_input("- Name (str): ", allowed='str')
            manual['mass'] = listing_input("- Mass (int): ")
            manual['position_x'] = listing_input("- Starting position (x): ")
            manual['position_y'] = listing_input("- Starting position (y): ")

            system_input[manual['name']] = (
                int(manual['mass']), (int(manual['position_x']), int(manual['position_y'])), manual['name'], int(int(manual['mass']) / 100)
            )
        except ValueError as E:
            if E.__str__() == 'Exit':
                user_exit = True
                print("Choice validated.")
            else:
                print("(!) - Value error; input anew.\n")

        except Exception as E:
            print("(?) - Something else went wrong (" + str(E) + "). Enter anew element.\n")

else:
    if not user_mode:
        print("# Mode selected: [default] (use default value)")
    else:
        print("# Mode selected: default (use default value)")

    system_input["Plan1"] = (500, (445, 560), "Plan1", 5)
    system_input["Plan2"] = (400, (440, 450), "Plan2", 4)
    system_input["Plan3"] = (300, (425, 400), "Plan3", 3)
    system_input["Plan4"] = (300, (400, 350), "Plan4", 6)


if not system_input:
    print("# (!) - Empty system.")
elif len(system_input) == 1:
    print("# (!) - One element system.")

print("Starting...")

# Completion
SIM: Board = Board(width=1000, height=1000, title="Simulation", fps=30, edges="bounce",
                   system=system_input, mass_softener=100, gravitational_constant=(6.67*(10**1)),
                   exponent_softener=-0.3, bounce_factor=0.9)

print("---\nEnd")




