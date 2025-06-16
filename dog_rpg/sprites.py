import pygame
from config import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change, self.y_change = 0, 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = 'down'

        self.exp = 0
    
    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change, self.y_change = 0, 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.health = 20
    
    def update(self):
        self.checkdeath()
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        distance_x = self.game.player.rect.x - self.rect.x
        distance_y = self.game.player.rect.y - self.rect.y
        distance_total = max(0.1, math.sqrt((distance_x)**2 + (distance_y)**2))
        distance_x, distance_y = distance_x/distance_total, distance_y/distance_total

        self.x_change = ENEMY_SPEED * distance_x
        self.y_change = ENEMY_SPEED * distance_y

    def checkdeath(self):
        if self.health <= 0:
            self.game.player.exp += 10
            self.kill()

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, x, y, dir):
        self.game = game
        self.groups = self.game.all_sprites
        self._layer = PLAYER_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE // 2
        self.height = TILESIZE // 2

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.x_change, self.y_change = 0, 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.time = 0
        self.ball_life = 120 #Ball travels for 2 seconds
        self.ball_damage = 20

        self.direction = dir
    
    def update(self):
        self.movement()
        self.collide()
        self.checkdeath()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change, self.y_change = 0, 0

    def movement(self):
        if self.direction == 'up':
            self.y_change -= BALL_SPEED
        if self.direction == 'down':
            self.y_change += BALL_SPEED
        if self.direction == 'right':
            self.x_change += BALL_SPEED
        if self.direction == 'left':
            self.x_change -= BALL_SPEED
    
    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        for enemy in hits:
            enemy.health -= self.ball_damage
            self.kill()
    
    def checkdeath(self):
        self.time += 1
        if self.time >= self.ball_life:
            self.kill()
