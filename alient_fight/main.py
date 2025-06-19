import pygame
from sprites import *
from config import *
from skilltree import *
from tilemaps import *
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.rows = WIN_HEIGHT // TILESIZE
        self.cols = WIN_WIDTH // TILESIZE

        self.skill_tree_open = False

        self.font = pygame.font.Font(None, 36)


        self.SPAWNENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWNENEMY, 2000)

        #Characters/Game Elements
        self.character_front_spritesheet = Spritesheet("./img/front_walk.png")
        self.character_back_spritesheet = Spritesheet("./img/back_walk.png")
        self.bullet_spritesheet = Spritesheet("./img/bullet.png")
        self.enemy_spritesheet = Spritesheet("./img/enemy.png")

        #Environment
        self.sand_bg_spritesheet = Spritesheet("./img/sand_bg.png")
        self.sand_bg = Background(self.sand_bg_spritesheet)

        skill_tree_root.val.x = WIN_WIDTH // 2
        skill_tree_root.val.y = TILESIZE
        self.layout_relative_to_parent(skill_tree_root, skill_tree_root.val.x, skill_tree_root.val.y, 2 * TILESIZE)
    
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 4, 4)

        self.createtilemap()
    
    def createtilemap(self):
        for i in range(self.rows):
            for j in range(self.cols):
                Ground(self, j, i, self.sand_bg)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == self.SPAWNENEMY:
                if not self.skill_tree_open:
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

        score_surf = self.font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        score_rect = score_surf.get_rect(topleft=(10, 10))
        self.screen.blit(score_surf, score_rect)

        
        self.clock.tick(FPS)
        pygame.display.update()
    
    def drawskilltree(self):

        skill_tree_text = self.font.render("Skilltree!", True, (255, 255, 255))
        skill_tree_text_rect = skill_tree_text.get_rect(center=(WIN_WIDTH//2, WIN_HEIGHT//2))

        def draw_node(node):
            if node is None:
                return

            if node.left:
                pygame.draw.line(
                    self.screen, (255, 255, 255),
                    (node.val.x, node.val.y),
                    (node.left.val.x, node.left.val.y), 2
                )
                draw_node(node.left)

            if node.right:
                pygame.draw.line(
                    self.screen, (255, 255, 255),
                    (node.val.x, node.val.y),
                    (node.right.val.x, node.right.val.y), 2
                )
                draw_node(node.right)
            
            node.val.draw(self.screen)


        draw_node(skill_tree_root)
        self.screen.blit(skill_tree_text, skill_tree_text_rect)

    def layout_relative_to_parent(self, node, x, y, x_spacing):
        if node is None:
            return

        node.val.x = x
        node.val.y = y

        if node.left:
            self.layout_relative_to_parent(node.left, x - x_spacing, y + TILESIZE * 2, x_spacing // 2)

        if node.right:
            self.layout_relative_to_parent(node.right, x + x_spacing, y + TILESIZE * 2, x_spacing // 2)


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

