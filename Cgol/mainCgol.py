"""
Conway's Game of Life

"""

# General configuration

import time

global Grid
global Run
global FPS
global Frames
global Delta

global WINDOW_HEIGHT
global WINDOW_WIDTH
global CHAR_ALIVE
global CHAR_DEAD


Grid: dict[int, dict[int, bool]] = {} # All coordinate stockpiled here. So for x, y access Grid[x][y]
Run: bool = True
FPS: int = 1
Frames: int = 0
Delta: float = 0.0

WINDOW_HEIGHT: int = 35
WINDOW_WIDTH: int = 20
CHAR_ALIVE: str = "@"
CHAR_DEAD: str = "."

# Game settings

global NEIGHBOURS_TO_BORN
global NEIGHBOURS_MIN
global NEIGHBOURS_MAX

NEIGHBOURS_TO_BORN = 3 # Exact number for a blank to go alive
NEIGHBOURS_MIN = 2 # Inclusive number of neighbours to not die of starvation
NEIGHBOURS_MAX = 3 # Inclusive number of neighbours to not die of overcrowd 

# Flags

global COMPLETE_VOID

COMPLETE_VOID = False


def grid_set(tiles: list[tuple[int, int]], state: bool = True, Grid_updated: dict[int, dict[int, bool]] = Grid) -> dict[int, dict[int, bool]]:
    for tile in tiles:
        if tile[0] not in Grid:
            Grid_updated[tile[0]] = {}
            
        if tile[1] not in Grid:
            Grid_updated[tile[0]][tile[1]] = state
        else:
            Grid_updated[tile[0]][tile[1]] = state
    
    return Grid_updated
    

def neighbours(coords: tuple[int, int], COMPLETE_VOID: bool = COMPLETE_VOID) -> int:
    """
    Find all the neighbours and react to them
    """
    RELATIVE_NEIGHBOURS_COORDS = (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    )
    
    neighbours_count: int = 0
    
    for neighbour in RELATIVE_NEIGHBOURS_COORDS:
        try:
            if Grid[coords[0] + neighbour[0]][coords[1] + neighbour[1]] is True:
                neighbours_count += 1
        
        except KeyError:
            # Create dead tiles if finds non existant tiles
            if COMPLETE_VOID:
                Grid[coords[0] + neighbour[0]] = {( coords[1] + neighbour[1]): False}
                
    return neighbours_count
                

def updater() -> dict[int, dict[int, bool]]:
    """
    Update position and states
    """
    Grid_new: dict[int, dict[int, bool]] = {}
    
    for x, cols in Grid.items():        
        for y, states in cols.items():
            if Grid[x][y] is True:
                if neighbours((x, y)) < NEIGHBOURS_MIN:
                    grid_set((x, y), False, Grid_new)
                elif neighbours((x, y)) > NEIGHBOURS_MAX:
                    grid_set((x, y), False, Grid_new)
            else:
                if neighbours((x, y)) == NEIGHBOURS_TO_BORN:
                    grid_set((x, y), True, Grid_new)
    
    return Grid_new
    

def drawer(camera_position: tuple[int, int],
           WINDOW_HEIGHT: int = WINDOW_HEIGHT, 
           WINDOW_WIDTH: int = WINDOW_WIDTH
           ) -> None:
    """
    Drawes (prints) the game board
    """
    
    Grid_drawn: list[list[bool]] = []

    # Iterate throught the whole grid
    for x_relative in range(WINDOW_WIDTH):
        Grid_drawn_record: list[bool] = []
        x_absolute: int = x_relative + camera_position[0]
        
        for y_relative in range(WINDOW_HEIGHT):
            y_absolute: int = y_relative + camera_position[1]
            try:
                Grid_drawn_record.append(Grid[x_absolute][y_absolute])
                
                if Grid[x_absolute][y_absolute] is True:
                    print(CHAR_ALIVE, end="")
                else:
                    print(CHAR_DEAD, end="")
            
            except KeyError:
                print(CHAR_DEAD, end="")
                if COMPLETE_VOID:
                    Grid[x_absolute] = {y_absolute: False}
                    
            
        Grid_drawn.append(Grid_drawn_record)
        print()
        
        
                
# Main exec
if __name__ == "__main__":
    print("# Starting X Cgol")
    print("## Setting init tiles")
    grid_set(
        tiles=[
            (0,1),
            (1,1),
            (1,2)
         ],
        state=True
    )
    
    while Run:
        
        print("### Frame", Frames)
        drawer(camera_position=(0, 0))
        Grid = updater()
        
        time.sleep(1/FPS)
        
        Frames += 1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                           