import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./test/08.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)  # full size of our image
        self.hit_box = self.rect.inflate(0, -10)  # changing the size of the image for overlapping
