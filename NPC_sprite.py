import pygame
import random
from Map_final import *
from SettingsINITIAL_final import *
from Sprites_final import *
from Player_final import *

class NPC():
    def __init__(self, game, screen):
        animation_time = 120
        self.screen = screen
        screen_width, screen_height = self.screen.get_size()

        self.x = random.randint(100, screen_width - 100)
        self.y = random.randint(100, screen_height - 100)

        super().__init__(game, self.x, self.y)
        self.screen = screen
        self.game = game





        self.soldier_sprite = pygame.image.load('Sprites\\Original_sprite.png').convert_alpha()
        self.soldier_pain = pygame.image.load('Sprites\\pain.png').convert_alpha()

        self.soldier_walk1 = pygame.image.load('Sprites\\walk1.png').convert_alpha()
        self.soldier_walk2 = pygame.image.load('Sprites\\walk2.png').convert_alpha()
        self.soldier_walk3 = pygame.image.load('Sprites\\walk3.png').convert_alpha()
        self.soldier_walk4 = pygame.image.load('Sprites\\walk4.png').convert_alpha()

        self.soldier_idle1 = pygame.image.load('Sprites\\idle1.png').convert_alpha()
        self.soldier_idle2 = pygame.image.load('Sprites\\idle2.png').convert_alpha()
        self.soldier_idle3 = pygame.image.load('Sprites\\idle3.png').convert_alpha()
        self.soldier_idle4 = pygame.image.load('Sprites\\idle4.png').convert_alpha()
        self.soldier_idle5 = pygame.image.load('Sprites\\idle5.png').convert_alpha()
        self.soldier_idle6 = pygame.image.load('Sprites\\idle6.png').convert_alpha()
        self.soldier_idle7 = pygame.image.load('Sprites\\idle7.png').convert_alpha()
        self.soldier_idle8 = pygame.image.load('Sprites\\idle8.png').convert_alpha()

        self.soldier_attack1 = pygame.image.load('Sprites\\Soldier_attack1.png').convert_alpha()
        self.soldier_attack2 = pygame.image.load('Sprites\\Soldier_attack2.png').convert_alpha()

        self.soldier_death1 = pygame.image.load('Sprites\\death1.png').convert_alpha()
        self.soldier_death2 = pygame.image.load('Sprites\\death2.png').convert_alpha()
        self.soldier_death3 = pygame.image.load('Sprites\\death3.png').convert_alpha()
        self.soldier_death4 = pygame.image.load('Sprites\\death4.png').convert_alpha()
        self.soldier_death5 = pygame.image.load('Sprites\\death5.png').convert_alpha()
        self.soldier_death6 = pygame.image.load('Sprites\\death6.png').convert_alpha()
        self.soldier_death7 = pygame.image.load('Sprites\\death7.png').convert_alpha()
        self.soldier_death8 = pygame.image.load('Sprites\\death8.png').convert_alpha()

        self.idle_frames = [self.soldier_idle1, self.soldier_idle2, self.soldier_idle3, self.soldier_idle4, self.soldier_idle5, self.soldier_idle6, self.soldier_idle7, self.soldier_idle8]


        self.health = 100
        self.attack_damage = 15
        self.speed = 3
        self.attack_distance = None
        self.size = 8
        self.health_damage = None
        self.animating = False
        self.animation_type = 'idle'
        self.current_frame = 0

    def get_current_frame(self):
        return self.idle_frames[self.current_frame]


    def load_animation(self):
        pass


    def update(self):
        self.check_animation_time()
        self.get_sprite()

    def render(self):
        frame = self.idle_frames[self.current_frame]
        dx = self.x - self.game.player.x
        dy = self.y - self.game.player.y
        distance = math.hypot(dx, dy)

        # Optional: check if NPC is within field of view
        if distance < self.game.render_distance:
            screen_x = self.x - self.game.player.x + self.screen.get_width() // 2
            screen_y = self.y - self.game.player.y + self.screen.get_height() // 2
            self.screen.blit(frame, (screen_x, screen_y))


    def attack(self):
        pass

    def death(self):
        pass

    def walk(self):
        pass

    def idle(self):
        pass

    def health(self):
        pass




