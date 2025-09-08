import pygame
from SettingsINITIAL_final import *
import math


class SpriteObject:
    def __init__(self, game, player, x, y, color=(255, 255, 255), size=32):
        self.game = game
        self.player = player

        # Sprite position
        self.x = screenWidth / 2
        self.y = screenHeight / 2  # centre of screen

        # Create a simple colored square instead of loading image
        self.image = pygame.Surface((size, size))
        self.image.fill(color)

        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.IMAGE_WIDTH // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()

        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0

        self.SPRITE_SCALE = 0.75
        self.SPRITE_HEIGHT_SHIFT = 0.2

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        image = pygame.transform.scale(self.image, (int(proj_width), int(proj_height)))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.SPRITE_HEIGHT_SHIFT
        render_pos = self.screen_x - self.sprite_half_width, screenHeight // 2 - proj_height // 2 + height_shift

        self.game.Raycasting.objects_to_render.append((self.norm_dist, image, render_pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.rotationAngle
        if (dx > 0 and self.player.rotationAngle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / (FOV / NumRays)
        self.screen_x = (NumRays // 2 + delta_rays) * Resolution

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)

        if -self.IMAGE_HALF_WIDTH < self.screen_x < (screenWidth + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class AnimatedSprite(SpriteObject):
    def __init__(self, game, x, y, colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255)], size=32):
        # Start with first color
        super().__init__(game, x, y, colors[0], size)

        self.colors = colors
        self.current_color_index = 0
        self.animation_time_prev = pygame.time.get_ticks()
        self.animation_trigger = False
        self.size = size

        # Animation speed
        self.ANIMATION_TIME = 500  # milliseconds between color changes

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate()

    def animate(self):
        if self.animation_trigger:
            # Cycle through colors
            self.current_color_index = (self.current_color_index + 1) % len(self.colors)
            current_color = self.colors[self.current_color_index]

            # Update the sprite image with new color
            self.image.fill(current_color)

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pygame.time.get_ticks()
        if time_now - self.animation_time_prev > self.ANIMATION_TIME:
            self.animation_time_prev = time_now
            self.animation_trigger = True