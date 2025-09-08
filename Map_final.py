import pygame
from SettingsINITIAL_final import *
_= False
MAP = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1,],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1,],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1,],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],

]

class Map:
    def __init__(self,Game):
        # Name: __init__
        # Parameters: self,Game
        # Returns: None
        # Purpose: Constructor to set up the initial values of the map
        self.Game = Game
        self.Map = MAP

    def has_wall_at(self, x, y):
        # Name: has_wall_at
        # Parameters: self,x,y
        # Returns:  returns False if tile_x < 0 or tile_x >= max_x or tile_y < 0 or tile_y >= max_y is true and if not self.Map[tile_y][tile_x] == 1
        # Purpose: To check to see if that position of the map has a wall there or open space
        max_y = len(self.Map)
        max_x = len(self.Map[0])
        tile_x = int(x // tile_size_x)
        tile_y = int(y // tile_size_y)
        if tile_x < 0 or tile_x >= max_x or tile_y < 0 or tile_y >= max_y:
            return False
        return self.Map[tile_y][tile_x] == 1

    def get_wall_type_at(self, x, y):
        # Name: get_wall_type_at
        # Parameters: self,x,y
        # Returns: returns self.Map[tile_y][tile_x] if if 0 <= tile_x < len(self.Map[0]) and 0 <= tile_y < len(self.Map) is true else it returns 0
        # Purpose: To check to see if that position of the map has a wall there or open space
        tile_x = int(x // tile_size_x)
        tile_y = int(y // tile_size_y)
        if 0 <= tile_x < len(self.Map[0]) and 0 <= tile_y < len(self.Map):
            return self.Map[tile_y][tile_x]
        return 0  # 0 means no wall


    def draw(self):
        # Name: draw
        # Parameters: self
        # Returns: None
        # Purpose: To loop through each row of the map and draw a wall if the value is 1
        for j in range(len(self.Map)):
            row = self.Map[j]
            for i in range(len(row)):
                tile = row[i]
                if tile == 1:
                    pygame.draw.rect(self.Game.screen,(0,0,0), pygame.Rect(i*tile_size_x, j*tile_size_y, tile_size_x -1, tile_size_y -1 ))

    # def walkable(self):
    #     walkable = []
    #     for y in range(len(self.Map)):
    #         for x in range(len(self.Map[0])):
    #             tile =self.Map[y][x]
    #             if tile == 0:
    #                 walkable.append((x,y))
    #     return walkable
    # def Map_Generation(self):







