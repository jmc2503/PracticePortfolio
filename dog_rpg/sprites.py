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

        self.speed = 3
        self.x_change, self.y_change = 0, 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = 'down'

        self.exp = 0
        self.level = 1
    
    def update(self):
        self.movement()
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

        font = pygame.font.SysFont(None, 12)
        text = font.render(self.name, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)
    
    def is_clicked(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx*dx + dy*dy <= self.radius*self.radius


def increase_dog_speed(self):
    self.player.speed += 3

shield_buff = SkillNode(None, "Shield", None)
ball_plus = SkillNode(shield_buff, "Ball+", None)
dog_speed = SkillNode(shield_buff, "Speed", increase_dog_speed)




skill_list = [shield_buff, ball_plus, dog_speed]

ball_plus_tree = TreeNode(ball_plus, None, None)
dog_speed_tree = TreeNode(dog_speed, None, None)
skill_tree_root = TreeNode(shield_buff, dog_speed_tree, ball_plus_tree)
