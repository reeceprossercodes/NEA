
import pygame
from Rendering_final import *

from SettingsINITIAL_final import *
from Map_final import *
from Player_final import *
import math
import sys
from NPC_sprite import *



def AngleConvert(angle):
    # Name: angleConvert
    # Parameters: angle
    # Returns: angle
    # Purpose: # takes in an angle as radians and returns the same angle within range of 0 to 2 pie
    #  if angle is less than 0 then 2 pie would be added to get it in its desired range

    angle =angle % (2*math.pi)
    if (angle < 0):
        angle = angle + 2*math.pi
    return angle

def Distance_inbetween(x1,x2,y1,y2):
    # Name: Distance_inbetween
    # Parameters: x1,x2,y1.y2
    # Returns: Distance using the equation math.sqrt((x2-x1)**2+(y2-y1)**2)
    # Purpose: calculates the distance between 2 points to work out the horizontal and vertical distance
    return math.sqrt((x2-x1)**2+(y2-y1)**2)







class Ray:
    # Name: Ray
    # Purpose: To work the rays
    def __init__(self, angle, player, map):
        # Name: __init__
        # Parameters: self, angle, player, map
        # Returns: None
        # Purpose: Constructor to set up the initial values of the ray
        self.angle = AngleConvert(angle)
        self.player = player
        self.Map = map
        self.facing_down = self.angle >= 0 and self.angle <= math.pi  # sees if its in the lower half of the circle
        self.facing_up = not self.facing_down
        self.facing_right = self.angle <= 0.5 * math.pi or self.angle >= 1.5 * math.pi # sees if its in the right half of the circle
        # less than pie/2 or greater than 3 pie/ 2
        self.facing_left = not self.facing_right
        # y axis goes down as it increases so its all flipped in pygame
        self.wall_type = 1




        self.wall_hit_x = 0
        self.wall_hit_y = 0

        self.distance = 0

        self.colour = 255

        self.hit_vertical = False

    def cast(self):
        # Name: cast
        # Parameters: self
        # Returns: None
        # Purpose: Casts the ray
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None

        if self.facing_up:
            first_intersection_y =  ((self.player.y // tile_size_y) * tile_size_y - 1)
        elif self.facing_down:
            first_intersection_y = ((self.player.y // tile_size_y) * tile_size_y + tile_size_y)

        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.angle)

        next_horizontal_intersection_x = first_intersection_x
        next_horizontal_intersection_y = first_intersection_y

        Ya = 0
        Xa = 0

        if self.facing_up:
            Ya = -tile_size_y
        elif self.facing_down:
            Ya = tile_size_y

        Xa = Ya / math.tan(self.angle)


        while (next_horizontal_intersection_x <= screenWidth and next_horizontal_intersection_x >= 0
        and next_horizontal_intersection_y >= 0 and next_horizontal_intersection_y <= screenHeight):
            if self.Map.has_wall_at (next_horizontal_intersection_x, next_horizontal_intersection_y):
                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_intersection_x
                horizontal_hit_y = next_horizontal_intersection_y
                self.wall_type = self.Map.get_wall_type_at(horizontal_hit_x, horizontal_hit_y)
                break

            else:
                next_horizontal_intersection_x += Xa
                next_horizontal_intersection_y += Ya











        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0

        if self.facing_right:
            vertical_hit_x = ((self.player.x // tile_size_x) * tile_size_x + tile_size_x )
        elif self.facing_left:
            vertical_hit_x = ((self.player.x // tile_size_x) * tile_size_x - 0.00001)

        first_intersection_y = (self.player.y + (vertical_hit_x - self.player.x) * math.tan(self.angle))


        next_vertical_intersection_x = vertical_hit_x
        next_vertical_intersection_y = first_intersection_y

        if self.facing_right:
            Xa = tile_size_x
        elif self.facing_left:
            Xa = -tile_size_x

        Ya = Xa * math.tan(self.angle)

        while (next_vertical_intersection_x <= screenWidth and next_vertical_intersection_x >= 0
               and next_vertical_intersection_y <= screenHeight and next_vertical_intersection_y >= 0):
            if self.Map.has_wall_at (next_vertical_intersection_x, next_vertical_intersection_y):
                found_vertical_wall = True
                vertical_hit_x = next_vertical_intersection_x
                vertical_hit_y = next_vertical_intersection_y
                self.wall_type = self.Map.get_wall_type_at(vertical_hit_x, vertical_hit_y)
                break

            else:
                next_vertical_intersection_x += Xa
                next_vertical_intersection_y += Ya






            #calculate distance

        horizontal_distance = 0
        vertical_distance = 0
        if found_horizontal_wall:
            horizontal_distance = Distance_inbetween(self.player.x, horizontal_hit_x, self.player.y, horizontal_hit_y)
        else:
            horizontal_distance = 10000   # allows it to be not valid without crashing

        if found_vertical_wall:
            vertical_distance = Distance_inbetween(self.player.x, vertical_hit_x, self.player.y, vertical_hit_y)
        else:
            vertical_distance = 10000

        if horizontal_distance < vertical_distance:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.distance = horizontal_distance
            self.colour = 160
            self.hit_vertical = False

        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.distance = vertical_distance
            self.colour = 255
            self.hit_vertical = True


        self.distance *= math.cos(self.player.rotationAngle - self.angle)   #fisheye correction elminates the curviness of the lines

        self.colour *= (70 / self.distance)    # light goes brighter when closer and darker when further
        if self.colour > 255:
            self.colour = 255
        elif self.colour < 0:
            self.colour = 0






    def render(self, screen):
        # Name: render
        # Parameters: screen self
        # Returns: None
        # Purpose: Draws the line that projects using the start position and end position

        # end_x = self.player.x + math.cos(self.angle) * 50
        # end_y = self.player.y + math.sin(self.angle) * 50
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.wall_hit_x, self.wall_hit_y))
        # self.Map = Map


class Raycasting:
    # Name: Raycasting
    # Purpose: Allows it to project 3D with me coding in 2D
    def __init__(self, game, player, map, renderer, npc):
        # Name: __init__
        # Parameters: self, game, player, map, renderer
        # Returns: None
        # Purpose: constructor to set up the initial values
        self.game = game
        self.rays = []
        self.player = player
        self.map = map
        self.renderer = renderer
        self.objects_to_render = []
        self.npc = npc


    def castRays(self):
        # Name: castRays
        # Parameters: self
        # Returns: None
        # Purpose: Casts the rays on the screen in the FOV
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV/2
        for j in range(NumRays):
            ray = Ray(rayAngle,self.player, self.map)
            ray.cast()
            self.rays.append(ray)
            rayAngle += FOV/NumRays




    def render(self, screen):
        # Name: render
        # Parameters: self, screen
        # Returns: None
        # Purpose: Renders the raycasting and also the texture
        count = 0
        for ray in self.rays:
            Distance_safe = max(ray.distance, 0.2)
            LineHeight = (tile_size_y / Distance_safe) * screenHeight
            LineHeight = min(LineHeight, screenHeight)
            draw_start = max(0, (screenHeight / 2) - LineHeight / 2)


            texture = self.renderer.textures.get(ray.wall_type, self.renderer.textures[1])
            texture_width = texture.get_width()

            # draw_end = LineHeight
            #         # Fisheye_correction = draw_start / math.cos(ray.distance - self.player.turnDirection)
            if ray.hit_vertical:
                hit_point = ray.wall_hit_y % tile_size_y
                texture_column_index = int((hit_point / tile_size_y) * texture_width)
            else:
                hit_point = ray.wall_hit_x % tile_size_x
                texture_column_index = int((hit_point / tile_size_x) * texture_width)

            texture_column_index = max(0, min(texture_column_index, texture_width - 1))


            column_surface = pygame.Surface((1, texture.get_height()), pygame.SRCALPHA)      # collumn rendering

            column_surface.blit(texture, (0, 0), area=pygame.Rect(texture_column_index, 0, 1, texture.get_height()))

            scaled_column = pygame.transform.scale(column_surface, (Resolution, int(LineHeight)))

            screen.blit(scaled_column, (count * Resolution, draw_start))
            count += 1

        for npc in self.game.npcs:
            dx = npc.x - self.player.x
            dy = npc.y - self.player.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            angle_to_npc = math.atan2(dy, dx)
            angle_diff = AngleConvert(angle_to_npc - self.player.rotationAngle)

            if abs(angle_diff) > FOV / 2:
                continue  # NPC is outside field of view

            screen_x = (angle_diff / FOV) * screenWidth
            sprite_size = min(screenHeight, (tile_size_y / distance) * screenHeight)
            sprite = pygame.transform.scale(npc.get_current_frame(), (sprite_size, sprite_size))

            ground_y = screenHeight // 2 + sprite_size // 2
            screen.blit(sprite, (screen_x - sprite_size // 2, ground_y - sprite_size))



