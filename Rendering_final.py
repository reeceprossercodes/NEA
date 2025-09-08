from Final_Raycasting import *
from Map_final import *

class Renderer:
    def __init__(self,screen, game):
        # Name: __init__
        # Parameters: self,screen,game
        # Returns: None
        # Purpose: Constructor to set up the initial values of the Renderer
        self.screen = screen
        self.game = game
        self.textures = self.load_texture()
        self.sky_offset = 0

    def load_texture(self):
        # Name: load_texture
        # Parameters: self
        # Returns: A dictionary for the textures correlating to numbers
        # Purpose: Loads the texture for the walls
        texture1 = pygame.image.load('Sprites\\Wall_texture1.png').convert_alpha()
        texture2 = pygame.image.load('Sprites\\Wall_texture2.png').convert_alpha()
        sky_texture = pygame.image.load('Sprites\\sky.png').convert_alpha()
        sky_texture = pygame.transform.scale(sky_texture, (screenWidth, HalfHeight))
        return {
            1: texture1,
            2: texture2,
            'Sky': sky_texture,
        }

    def draw_sky(self):
        # Name: draw_sky
        # Parameters: self
        # Returns: None
        # Purpose: To add the sky to the game
        if self.game.player.turnDirection != 0:
            self.sky_offset = (self.sky_offset + 4 * self.game.player.turnDirection) % screenWidth

        self.screen.blit(self.textures['Sky'], (-self.sky_offset, 0))
        self.screen.blit(self.textures['Sky'], (screenWidth - self.sky_offset, 0))

    def draw_floor(self):
        # Name: draw_floor
        # Parameters: self
        # Returns: None
        # Purpose: To set the floor to a colour
        pygame.draw.rect(self.screen, Floor_colour, (0,HalfHeight, screenWidth, screenHeight))
