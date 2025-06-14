import pygame
import random

WIDTH, HEIGHT = 300, 600
ROWS, COLS, = 20, 10
TILE = WIDTH // COLS
FPS = 60

BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
SHAPE_COLORS = [
    (0, 255, 255),   # I
    (0, 0, 255),     # J
    (255, 165, 0),   # L
    (255, 255, 0),   # O
    (0, 255, 0),     # S
    (160, 32, 240),  # T
    (255, 0, 0)      # Z
]

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],        # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]]   # Z
]

class Piece:
    def __init__(self, x, y):
        self.x = x
        self. y = y
        self.shape = random.choice(SHAPES)
        self.color = SHAPE_COLORS[SHAPES.index(self.shape)]
        self.rotation = 0
    
    def image(self):
        return self.shape

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
