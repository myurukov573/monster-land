import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'  

import pygame
import sys
from level import Level
from settings import *

class Game:
    def __init__(self):
        """Инициализира pygame, дисплей, часовник и звук"""
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"[AUDIO WARNING] Mixer init failed: {e}")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Monster Land')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        try:
            main_sound = pygame.mixer.Sound('./media/audio/main.ogg')
            main_sound.play(loops=-1)
        except pygame.error as e:
            print(f"[AUDIO WARNING] Could not load or play sound: {e}")

    def run(self):
        """Основният игрови цикъл"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
