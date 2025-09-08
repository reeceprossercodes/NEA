from SettingsINITIAL_final import *
from Rendering_final import *
import pygame





class Weapon:
    # Name: Weapon
    # Purpose: Set up the weapon
    def __init__(self,screen,game):
        # Name: __init__
        # Parameters: self, screen, game
        # Returns: None
        # Purpose: Constructor to set up the initial values of the map

        self.screen = screen
        self.game = game

        self.damage_headshot = 50
        self.damage_bodyshot = 50
        self.damage_legshot = 50
        self.reloading = False
        self.animating = False
        self.animation_type = 0
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 100


        self.shotgun_firing1 = pygame.image.load("Sprites\\0.png").convert_alpha()
        self.shotgun_firing2 = pygame.image.load("Sprites\\1.png").convert_alpha()
        self.shotgun_firing3 = pygame.image.load("Sprites\\2.png").convert_alpha()
        self.reloading1 = pygame.image.load("Sprites\\3.png").convert_alpha()
        self.reloading2 = pygame.image.load("Sprites\\4.png").convert_alpha()
        self.reloading3 = pygame.image.load("Sprites\\5.png").convert_alpha()
        weapon_height = self.shotgun_firing1.get_height()
        self.weapon_position = (HalfWidth, screen.get_height() - weapon_height //1.51)

        self.shotgun_frames = [self.shotgun_firing1,self.shotgun_firing2,self.shotgun_firing3]
        self.reloading_frames = [self.reloading1,self.reloading2,self.reloading3]


    def shooting(self):
        # Name: shooting
        # Parameters: self
        # Returns: None
        # Purpose: swithces to the shooting images when not animating
        if not self.animating:
            self.animating = True
            self.animation_type = 'shooting'
            self.current_frame = 0
            self.animation_timer = pygame.time.get_ticks()


    def draw(self):
        # Name: draw
        # Parameters: self
        # Returns: None
        # Purpose: Switches the images on the screen so when the gun is shot it will go from the shooting pictures to the reloading
        if self.animating:
            if self.animation_type == 'shooting':
                frame = self.shotgun_frames[self.current_frame]
            elif self.animation_type == 'reloading':
                frame = self.reloading_frames[self.current_frame]

            else:
                frame = self.shotgun_frames[0]
        else:
            frame = self.shotgun_frames[0]

        self.game.screen.blit(frame, self.weapon_position)


    def update(self):
        # Name: update
        # Parameters: self
        # Returns: None
        # Purpose: Switches the images on the screen so when the gun is shot it will go from the shooting pictures to the reloading
        if self.animating:
            ticks = pygame.time.get_ticks()
            if ticks - self.animation_timer > self.animation_speed:
                self.animation_timer = ticks
                self.current_frame += 1

                if self.animation_type == 'shooting':
                    if self.current_frame >= len(self.shotgun_frames):

                        self.animation_type = 'reloading'
                        self.current_frame = 0
                    return
                elif self.animation_type == 'reloading':
                    if self.current_frame >= len(self.reloading_frames):


                        self.animating = False
                        self.current_frame = 0
                        self.animation_type = 0




