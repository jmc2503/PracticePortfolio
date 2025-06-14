import pygame

#Initializing constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle for player and opponent
class Paddle:
    def __init__(self, color, speed=0, is_op=True):
        self.color = color #render color
        self.speed = speed #speed of paddle movement
        self.is_op = is_op #is this the player or the opponent?
        if self.is_op:
            self.rect = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        else:
            self.rect = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def move(self, ball=None):
        # If the paddle is controlled by the AI, it just moves towards the ball
        if self.is_op:
            if self.rect.top < ball.rect.y:
                self.rect.y += self.speed
            elif self.rect.bottom > ball.rect.y:
                self.rect.y -= self.speed 
        else:
            self.rect.y += self.speed
        
        self.rect.y = max(0, min(self.rect.y, HEIGHT - PADDLE_HEIGHT))


class Ball:
    def __init__(self, color):
        self.rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, BALL_RADIUS*2, BALL_RADIUS*2)
        self.color = color
        self.ball_dx = 5
        self.ball_dy = 5
    
    def move(self):
        self.rect.x += self.ball_dx
        self.rect.y += self.ball_dy

        # Check for collision with top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.ball_dy *= -1

        # Check for the ball passing boundaries -> reset position and update score
        if self.rect.left <= 0:
            global player_score
            player_score += 1
            self.rect.x, self.rect.y = WIDTH // 2, HEIGHT // 2
            self.ball_dx *= -1 
        
        if self.rect.right >= WIDTH:
            global opponent_score
            opponent_score += 1
            self.rect.x, self.rect.y = WIDTH // 2, HEIGHT // 2
            self.ball_dx *= -1

pygame.init()

# Scoreboard initialization
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 50)

# Initialize player, opponent, and ball
player = Paddle((255,0,0), 0, False)
opponent = Paddle((0, 0, 0), 5, True)
ball = Ball(BLACK)

# Initialize the screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

while True:
    #Check for events/inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed = -5
            if event.key == pygame.K_DOWN:
                player.speed = 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed = 0
    
    # move game objects
    ball.move()
    player.move()
    opponent.move(ball)

    # Check for collision with paddles
    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponent.rect):
        ball.ball_dx *= -1
    
    #Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, player.color, player.rect)
    pygame.draw.rect(screen, opponent.color, opponent.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 20, 20))
    screen.blit(opponent_text, (WIDTH // 2 - 40, 20))

    pygame.display.flip()
    clock.tick(60)



