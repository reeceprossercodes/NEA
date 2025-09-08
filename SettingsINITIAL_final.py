import pygame
import math



player_Pos = [5, 5]
player_Dir = [-3, 0]
player_Plane = [0, 1]

screenHeight = 1390
screenWidth = 2550
HalfHeight = screenHeight / 2
HalfWidth = screenWidth / 2
tile_size_x = 200
tile_size_y = 92

texture_size = 200
half_texture_size = texture_size // 2

FOV = math.radians(60)

Resolution= 3
NumRays = screenWidth // Resolution

screen = pygame.display.set_mode((screenWidth, screenHeight))

Floor_colour = (35,32,33)

SCREEN_DIST = screenWidth / (2 * math.tan(FOV / 2))
DELTA_ANGLE = FOV / NumRays
HALF_NUM_RAYS = NumRays // 2
SCALE = Resolution

