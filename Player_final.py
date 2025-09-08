import pygame
import math
from Map_final import *
from SettingsINITIAL_final import *

class Player:
    def __init__(self,gameMap):
        # Name: __init__
        # Parameters: self,gamemap
        # Returns: None
        # Purpose: Constructor to set up the initial values of the map
        self.map = gameMap
        self.x = screenWidth / 2
        self.y = screenHeight / 2 # centre of screen
        self.radius = 5
        self.rotationAngle = 90 * math.pi / 180 # radians
        self.moveSpeed = 4
        self.rotationSpeed = 1 * math.pi / 180
        self.turnDirection = 0

    def render(self, screen):
        # Name: render
        # Parameters: self, screen
        # Returns: None
        # Purpose: to draw the initial player shape and line
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)

        # pygame.draw.line(screen, (255,0,0), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50), 2)

    def move(self):
        # Name: move
         # Parameters: self
         # Returns: None
         # Purpose: to assign the keys with how the character will move and rotation
        keys = pygame.key.get_pressed()

        self.turnDirection = 0
        self.WalkDirection = 0

        if keys[pygame.K_d]:
            self.turnDirection = 1
        if keys[pygame.K_a]:
            self.turnDirection = -1
        if keys[pygame.K_w]:
            self.WalkDirection = 1
        if keys[pygame.K_s]:
            self.WalkDirection = -1

        Move= self.WalkDirection * self.moveSpeed    #calculates movement
        self.rotationAngle += self.turnDirection * self.rotationSpeed
        new_x = self.x + math.cos(self.rotationAngle) * Move
        new_y = self.y + math.sin(self.rotationAngle) * Move


        tile_x = int(new_x / tile_size_x) # puts into coordinates
        tile_y = int(new_y / tile_size_y)

        if 0 <= tile_y < len(self.map.Map) and 0 <= tile_x < len(self.map.Map[0]):
            if self.map.Map [tile_y][tile_x] == 0:
                self.x = new_x
                self.y = new_y






