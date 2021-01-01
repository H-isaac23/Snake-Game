import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.rect = pygame.rect.Rect(screen_width/2, screen_height/2 , 20, 20)

class Body(Snake):
    def __init__(self, vel, prev_x, prev_y):
        super().__init__()
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.rect.x = prev_x
        self.rect.y = prev_y
        self.vel = vel
        self.vel_x = self.vel
        self.vel_y = 0
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, body_color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.vel_y == 0:
            self.vel_x = 0
            self.vel_y -= self.vel
        if keys[pygame.K_DOWN] and self.vel_y == 0:
            self.vel_x = 0
            self.vel_y += self.vel
        if keys[pygame.K_LEFT] and self.vel_x == 0:
            self.vel_y = 0
            self.vel_x -= self.vel
        if keys[pygame.K_RIGHT] and self.vel_x == 0:
            self.vel_y = 0
            self.vel_x += self.vel

        self.constraint()

        self.prev_y = self.rect.y
        self.prev_x = self.rect.x
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        self.collide()

    def collide(self):
        if self.rect.colliderect(food.rect):
            food.active = False
            self.score += 1
        if len(whole_body) > 1:
            for i in range(1, len(whole_body)-1):
                if whole_body[0].rect == whole_body[i].rect:
                    game.game_restart()
                    break

    def constraint(self):
        if self.rect.x + self.vel_x <= 20:
            self.rect.x = 20
            game.game_restart()
        if self.rect.x + self.vel_x >= screen_width - 40:
            self.rect.x = screen_width - 40
            game.game_restart()
        if self.rect.y + self.vel_y <= 20:
            self.rect.y = 20
            game.game_restart()
        if self.rect.y + self.vel_y >= screen_height - 40:
            self.rect.y = screen_height - 40
            game.game_restart()

class Food:
    def __init__(self):
        self.radius = 20
        self.active = True
        self.x_pos = range(40, screen_width-40, 20)
        self.y_pos = range(40, screen_height-40, 20)
        self.rect = pygame.rect.Rect(self.x_pos[random.randint(0, 32)], self.y_pos[random.randint(0, 32)], self.radius, self.radius)

    def make_food(self):
        if self.active == False:
            self.rect.x = self.x_pos[random.randint(0, 32)]
            self.rect.y = self.y_pos[random.randint(0, 32)]

    def draw_food(self):
        self.active = True
        pygame.draw.ellipse(screen, (200, 200, 200), self.rect, self.radius)

class GameManager:
    def game_restart(self):

        for i in range(len(whole_body)-1):
            whole_body.pop()

        snake.rect.center = (90, 90)
        snake.vel_x = snake.vel
        snake.vel_y = 0

def body_mechanism():
    # Body movement mechanism
    whole_body[0].move()
    whole_body[0].draw()

    if len(whole_body) > 1:
        for i in range(1, len(whole_body)):
            whole_body[i].prev_y = whole_body[i].rect.y
            whole_body[i].prev_x = whole_body[i].rect.x
            whole_body[i].rect.x = whole_body[i - 1].prev_x
            whole_body[i].rect.y = whole_body[i - 1].prev_y
            whole_body[i].draw()

    food.make_food()

    if food.active == False:
        whole_body.append(Body(whole_body[-1].vel, whole_body[-1].prev_x, whole_body[-1].prev_y))


# Setting up the main window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Color
bg_color = pygame.Color('#2F373F')
body_color = (200, 200, 200)

# Game Objects
snake = Body(20, 100, 100)
whole_body = [snake]
food = Food()

# Game Manager
game = GameManager()

while True:
    for event in pygame.event.get():
        # Exiting the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    body_mechanism()
    food.draw_food()
    pygame.display.flip()
    clock.tick(15)