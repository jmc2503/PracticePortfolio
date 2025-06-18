import pygame
from sprites import *
from config import *
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.skill_tree_open = False

        self.SPAWNENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWNENEMY, 2000)
    
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 4, 4)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == self.SPAWNENEMY:
                x, y = self.randomspawn()
                Enemy(self, x, y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Ball(self, self.player.rect.x+TILESIZE//4, self.player.rect.y-TILESIZE//2, 'up')
                    if self.player.facing == 'down':
                        Ball(self, self.player.rect.x+TILESIZE//4, self.player.rect.y + TILESIZE//2, 'down')
                    if self.player.facing == 'left':
                        Ball(self, self.player.rect.x-TILESIZE//2, self.player.rect.y+TILESIZE//4, 'left')
                    if self.player.facing == 'right':
                        Ball(self, self.player.rect.x+TILESIZE//2, self.player.rect.y+TILESIZE//4, 'right')
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for skill in skill_list:
                    if skill.is_clicked(event.pos):
                        if not skill.unlocked:
                            skill.unlocked = True
                            skill.effect(self)
                            self.skill_tree_open = False

            

    def update(self):
        if not self.skill_tree_open:
            self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        if self.skill_tree_open:
            self.drawskilltree()
        
        self.clock.tick(FPS)
        pygame.display.update()
    
    def drawskilltree(self):
        x, y = 10, 1
        
        q = []
        q.append(skill_tree_root)
        curr_level = 0

        while q:
            len_q = len(q)
            spawn_x = x - 1.5*len_q

            for i in range(len_q):
                node = q.pop()
                node.val.x = (spawn_x + i * 2) * TILESIZE
                node.val.y = (y + curr_level * 1.5) * TILESIZE
                node.val.draw(self.screen)

                if node.val.parent:
                    pygame.draw.line(self.screen, (255, 255, 255), (node.val.x, node.val.y), (node.val.parent.x, node.val.parent.y), 2)


                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            
            curr_level += 1

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def randomspawn(self):
        side = random.randint(0, 3)
        x, y = 0, 0

        if side == 0: #spawn top
            x = random.randint(0, 19)
            y = 0
        elif side == 1: #spawn bottom
            x = random.randint(0, 19)
            y = 15
        elif side == 2: #spawn left
            x = 0
            y = random.randint(0, 14)
        elif side == 3: #spawn right
            x = 19
            y = random.randint(0, 14)
    
        return x, y

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit

