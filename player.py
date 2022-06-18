import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./test/attack_down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos) # full size of the image
        self.hit_box = self.rect.inflate(0, -60)  # changing the size of the image for overlapping

        self.direction = pygame.math.Vector2()  # by default x: 0 y: 0
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        """Player movement when we press the button"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            """when the key is not press setting up to 0 to stop moving"""

            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            """normalize the speed does not matter what direction is going always will be one"""
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * speed
        self.collision('horizontal')
        self.hit_box.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hit_box.center
        # self.rect.center += self.direction * speed

    def collision(self, direction):
        """Collision to obstacles"""
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                """Checking collision rectangle of sprite to rectangle of the player"""
                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.x > 0:  # moving right
                        """checking if the collision is in the right"""
                        """moving the right site of the player to the left site of the obstacle"""
                        self.hit_box.right = sprite.hit_box.left

                    if self.direction.x < 0:  # moving left
                        """checking if the collision is in the left"""
                        """moving the left site of the player to the right site of the obstacle"""
                        self.hit_box.left = sprite.hit_box.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                """Checking collision rectangle of sprite to rectangle of the player"""

                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.y > 0:  # moving down
                        """checking if the collision is it down"""
                        """moving the down site of the player to the up site of the obstacle"""
                        self.hit_box.bottom = sprite.hit_box.top

                    if self.direction.y < 0:  # moving up
                        """checking if the collision is it up"""
                        """moving the up site of the player to the down site of the obstacle"""
                        self.hit_box.top = sprite.hit_box.bottom

    def update(self):
        self.input()
        self.move(self.speed)
