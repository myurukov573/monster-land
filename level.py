from random import choice

import pygame

from settings import *
from support import import_csv_layout, import_folder
from tile import Tile
from player import Player
from debug import debug
from weapon import Weapon


class Level:
    """ contains all sprites (player, enemies, map, all the obstacles) also deal with their interactions"""

    def __init__(self):
        """visible sprites - group for sprites that will be drawn only group that draws sprites"""
        self.player = None
        """obstacle_sprites - group for sprites that the player can collide with"""
        # getting display surface anywhere from our code (like from main Game self.screen)
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()  # custom sprites Group
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        # sprite setup
        self.create_map()

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        else:
            self.current_attack = None

    def create_map(self):
        """ Creating a map using the WORLD_Map matrix if col is x will be a wall if it is p will be the player"""
        layouts = {
            'boundary': import_csv_layout('media/csv/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('media/csv/map/map_Grass.csv'),
            'object': import_csv_layout('media/csv/map/map_Objects.csv')
        }

        graphics = {
            'grass': import_folder('./media/grass'),
            'objects': import_folder('./media/objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TITLE_SIZE
                        y = row_index * TITLE_SIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            # create a grass tile
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            # create an object tile
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
        # for row_index, row in enumerate(WORLD_MAP):
        #     for col_index, col in enumerate(row):
        #         x = col_index * TITLE_SIZE
        #         y = row_index * TITLE_SIZE
        #         if col == 'x':
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         if col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites, self.create_attack,
                             self.destroy_attack)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    """First part: Function as a camera """
    """Second part: Y sort is going to sort the sprite by the Y coordinate that way will give them some overlap"""

    def __init__(self):
        super().__init__()
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('./media/tilemap/ground.png')
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # for sprite in self.sprites():
        """Sorting the sprite to be created first and drawing the all elements"""
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
