import pygame

from settings import *
from tile import Tile
from player import Player
from debug import debug


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
        # sprite setup
        self.create_map()

    def create_map(self):
        """ Creating a map using the WORLD_Map matrix if col is x will be a wall if it is p will be the player"""
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TITLE_SIZE
                y = row_index * TITLE_SIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

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

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        """Sorting the sprite to be created first"""
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
