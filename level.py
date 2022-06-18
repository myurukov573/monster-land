import pygame

from settings import *
from tile import Tile
from player import Player


class Level:
    """ contains all sprites (player, enemies, map, all the obstacles) also deal with their interactions"""

    def __init__(self):
        """visible sprites - group for sprites that will be drawn only group that draws sprites"""
        """obstacle_sprites - group for sprites that the player can collide with"""
        # getting display surface anywhere from our code (like from main Game self.screen)
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TITLE_SIZE
                y = row_index * TITLE_SIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    Player((x, y), [self.visible_sprites])

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
