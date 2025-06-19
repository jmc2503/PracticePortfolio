import pygame
from config import *
import math

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

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

        self.speed = 3
        self.x_change, self.y_change = 0, 0

        self.image = self.game.character_front_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = 'down'
        self.animation_loop = 1
        self.animation_speed = 0.3

        self.exp = 0
        self.level = 1

        self.items = []

        self.front_animations = [self.game.character_front_spritesheet.get_sprite(0,0, self.width, self.height),
                           self.game.character_front_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_front_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.character_front_spritesheet.get_sprite(32, 32, self.width, self.height)]
        
        self.back_animations = [self.game.character_back_spritesheet.get_sprite(0, 0, self.width, self.height),
                               self.game.character_back_spritesheet.get_sprite(32, 0, self.width, self.height),
                               self.game.character_back_spritesheet.get_sprite(0, 32, self.width, self.height),
                               self.game.character_back_spritesheet.get_sprite(32, 32, self.width, self.height)]
    
        self.score = 0

    def update(self):
        self.movement()
        self.animate()
        self.check_level()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change, self.y_change = 0, 0
    
    def check_level(self):
        if self.exp >= 20:
            self.level += 1
            self.exp = 0
            self.game.skill_tree_open = True

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= self.speed
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += self.speed
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= self.speed
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += self.speed
            self.facing = 'down'
    
    def animate(self):
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_back_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = self.back_animations[math.floor(self.animation_loop)]
                self.animation_loop += self.animation_speed
                if self.animation_loop >= 4:
                    self.animation_loop = 0
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_front_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = self.front_animations[math.floor(self.animation_loop)]
                self.animation_loop += self.animation_speed
                if self.animation_loop >= 4:
                    self.animation_loop = 0
        
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_front_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = self.front_animations[math.floor(self.animation_loop)]
                self.animation_loop += self.animation_speed
                if self.animation_loop >= 4:
                    self.animation_loop = 0

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_front_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = self.front_animations[math.floor(self.animation_loop)]
                self.animation_loop += self.animation_speed
                if self.animation_loop >= 4:
                    self.animation_loop = 0

        
    def check_items(self):
        pass

    
    def get_item(self, item):
        self.items.append(item)

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

        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.health = 20

        self.animation_loop = 0
        self.animation_speed = 0.3

        self.enemy_animations = [self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(32, 0, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(0, 32, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(32, 32, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(0, 64, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(32, 64, self.width, self.height),]
    
    def update(self):
        self.checkdeath()
        self.animate()
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
    
    def animate(self):
        self.image = self.enemy_animations[math.floor(self.animation_loop)]
        self.animation_loop += self.animation_speed
        if self.animation_loop >= 6:
            self.animation_loop = 0

    def checkdeath(self):
        if self.health <= 0:
            self.game.player.exp += 10
            self.game.player.score += 10
            self.kill()

class Ball(pygame.sprite.Sprite):

    speed = 5

    def __init__(self, game, x, y, dir):
        self.game = game
        self.groups = self.game.all_sprites
        self._layer = PLAYER_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE // 2
        self.height = TILESIZE // 2

        self.image = None

        self.x_change, self.y_change = 0, 0

        self.time = 0
        self.ball_life = 120 #Ball travels for 2 seconds
        self.ball_damage = 20
        self.ball_speed = Ball.speed

        self.direction = dir

        self.animation_loop = 0

        if self.direction == "left":
            self.bullet_animations = [pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -180),
                                  pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0, 16, self.width, self.height), -180)]
            self.image = pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -180)
        elif self.direction == "right":
            self.bullet_animations = [self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height),
                                  self.game.bullet_spritesheet.get_sprite(0, 16, self.width, self.height)]
            self.image = self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height)
        elif self.direction == "up":
            self.bullet_animations = [pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -270),
                                  pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0, 16, self.width, self.height), -270)]
            self.image = pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -270)
        elif self.direction == "down":
            self.bullet_animations = [pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -90),
                                  pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0, 16, self.width, self.height), -90)]
            self.image = pygame.transform.rotate(self.game.bullet_spritesheet.get_sprite(0,0,self.width,self.height), -90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.movement()
        self.animate()
        self.collide()
        self.checkdeath()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change, self.y_change = 0, 0

    def movement(self):
        if self.direction == 'up':
            self.y_change -= self.ball_speed
        if self.direction == 'down':
            self.y_change += self.ball_speed
        if self.direction == 'right':
            self.x_change += self.ball_speed
        if self.direction == 'left':
            self.x_change -= self.ball_speed
    
    def animate(self):
        self.image = self.bullet_animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.5
        if self.animation_loop >= 2:
            self.animation_loop = 0

    
    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        for enemy in hits:
            enemy.health -= self.ball_damage
            self.kill()
    
    def checkdeath(self):
        self.time += 1
        if self.time >= self.ball_life:
            self.kill()

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class SkillNode:
    def __init__(self, parent, name="Skill", effect=None):
        self.name = name
        self.x = 0
        self.y = 0
        self.radius = TILESIZE // 2
        self.unlocked = False
        self.unlockable = False
        self.effect = effect
        self.parent = parent

    def draw(self, screen):
        color = (0, 255, 0) if self.unlocked else (100, 100, 100)
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, 2)

        font = pygame.font.SysFont(None, 15)
        text = font.render(self.name, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)
    
    def is_clicked(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx*dx + dy*dy <= self.radius*self.radius

class Shield(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game

        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        
        self.x = TILESIZE * x
        self.y = TILESIZE * y
        self.width = TILESIZE + 5
        self.height = TILESIZE + 5

        self.image = pygame.Surface([self.width, self.height])



