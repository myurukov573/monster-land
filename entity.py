import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animations_speed = 0.15
        self.direction = pygame.math.Vector2()

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
