"""
Conway's Game of Life

"""

ax = []
ay = []

class Pos:
    def __init__(self, x, y):
        """
        Function: Load new pixel
        """
        self.x = x
        self.y = y
        self.state = False
        
        return True
    