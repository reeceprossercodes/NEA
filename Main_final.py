import sys

import pygame

# from Character import *
# from Character import *
from Player_final import *
from Final_Raycasting import *
from Rendering_final import *
from Weapon_sprite import *
from NPC_sprite import *

class Game:
    # Name: Game
    # Purpose: The games
    def __init__(self):
        # Name: __init__
        # Parameters: self
        # Returns: None
        # Purpose: Constructor to set up the initial values of the map
        pygame.init()
        self.screen = pygame.display.set_mode((2550, 1390), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.map = Map(self)
        self.player = Player(self.map)
        # self.npc = NPC(self.map)
        self.renderer = Renderer(self.screen, self)
        self.Raycasting = Raycasting(self, self.player, self.map,self.renderer, self.npc)
        self.weapon = Weapon(self.screen, self)

        # self.npc = NPC(self, self.screen)
        self.npc = [NPC(self, map)]
        self.npc_sprite = SpriteObject(self)





    def Clock(self):
        # Name: Clock
        # Parameters: self
        # Returns: None
        # Purpose: manage time and frame rate
        self.clock.tick(120)


    def draw(self):
        # Name: draw
        # Parameters: self
        # Returns: None
        # Purpose: to fill the screen and draw the map
        self.screen.fill((0, 0, 0))
        self.map.draw()

        self.renderer.draw_floor()
        self.renderer.draw_sky()

    def Weapon_draw(self):
        self.weapon.draw()

    # def NPC_draw(self):
    #     for npc in self.npcs:
    #         npc.draw()


    def Character(self):
        # Name: Character
        # Parameters: self
        # Returns: None
        # Purpose: Calls the character
        self.player.move()

    # def Enemy(self):
    #     # Name: draw
    #     # Parameters: self
    #     # Returns: None
    #     # Purpose: to fill the screen and draw the map
    #     self.npc.render(self.screen)
    #     self.npc.control()


    def Raycast(self):
        # Name: Raycast
        # Parameters: self
        # Returns: None
        # Purpose: Calls the raycast to cast the rays and to render on my screen

        # self.player.render(self.screen)
        self.Raycasting.castRays()
        self.Raycasting.render(self.screen)

    def exit(self):
        # Name: exit
        # Parameters: self
        # Returns: None
        # Purpose: to allow the user to exit the game tab without it crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    self.weapon.shooting()

    def run(self):
        # Name: run
        # Parameters: self
        # Returns: None
        # Purpose: to run all the functions
        while True:
            self.exit()
            self.Clock()
            self.draw()
            self.Character()
            # self.Enemy()
            self.Raycast()
            self.weapon.update()
            self.Weapon_draw()
            # self.NPC_draw()
            for npc in self.npcs:
                npc.update()


            pygame.display.flip()



if __name__ == '__main__':
    game = Game()
    game.run()
