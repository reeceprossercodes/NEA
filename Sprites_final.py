import pygame
from SettingsINITIAL_final import Resolution, NumRays, FOV, SCREEN_DIST, screenHeight, screenWidth
from Player_final import *
import math


class Sprites:
    def __init__(self, game, player, x, y):
        self.game = game
        self.player = player
        self.x = x
        self.y = y
        self.SPRITE_SCALE = 0.75
        self.SPRITE_HEIGHT_SHIFT = 0.2

        self.image = pygame.image.load('Sprites/Candle.png').convert_alpha()

        self.image_width = self.image.get_width()
        self.image_half_width = self.image_width // 2
        self.image_ratio = self.image_width / self.image.get_height()

        self.dx, self.dy = 0, 0  # Distance (player to sprite)
        self.theta = 0          # Angle (player to sprite)
        self.screen_x = 0   # Screen position to sprite
        self.dist = 1  # distance
        self.norm_dist = 1          # Fisheye correction
        self.sprite_half_width = 0  # Half width of sprite



        self.projected_this_frame = False



    def sprite_projection(self): # calulates how it appears on screen based on distance from the player
        projection = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        projection_width, projection_height = projection * self.image_ratio, projection
        image = pygame.transform.scale(self.image, (int(projection_width), int(projection_height)))

        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.SPRITE_HEIGHT_SHIFT
        render_position = self.screen_x - self.sprite_half_width, screenHeight // 2 - projection_height // 2 + height_shift





        self.game.Raycasting.objects_to_render.append((self.norm_dist, image, render_position))





    def get_sprite(self):   #whether the sprite is visible to the player prepares for rendering

        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.rotationAngle
        delta = (delta + math.pi) % (2 * math.pi) - math.pi

        delta_rays = delta / (FOV / NumRays)
        self.screen_x = (NumRays // 2 + delta_rays) * Resolution
        #calculates the distance and applys fisheye correction
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)

        if -self.image_half_width < self.screen_x < (screenWidth + self.image_half_width) and self.norm_dist > 0.5:
            self.sprite_projection()


    def update(self):
        self.get_sprite()



