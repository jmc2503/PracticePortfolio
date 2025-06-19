from sprites import *
from config import *
import random

class Background:
    def __init__(self, background_sheet):
        self.width = TILESIZE
        self.height = TILESIZE
        self.background_list = [background_sheet.get_sprite(0, 0, self.width, self.height),
                                background_sheet.get_sprite(32, 0, self.width, self.height),
                                background_sheet.get_sprite(0, 32, self.width, self.height),
                                background_sheet.get_sprite(32, 32, self.width, self.height),
                                background_sheet.get_sprite(0, 64, self.width, self.height)
                                ]

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, background):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = random.choice(background.background_list)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
