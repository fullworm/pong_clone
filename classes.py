import random
import math as m
import pygame

class Pong:
    def __init__(self, img_path, pos, screen_params):
        self.pong = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.pong_r = self.pong.get_rect(topleft=pos)
        self.movement = [False, False]
        self.screen_dims = screen_params

    def move(self):
        if self.movement[0]:
            self.pos[1] -= 7
        if self.movement[1]:
            self.pos[1] += 7

        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] + self.pong_r.height > self.screen_dims[1]:
            self.pos[1] = self.screen_dims[1] - self.pong_r.height

        self.pong_r.topleft = (self.pos[0], self.pos[1])


class Ball:
    def __init__(self, img_path, screen_params):
        self.ball = pygame.image.load(img_path).convert_alpha()
        self.screen_dims = screen_params
        self.ball_r = self.ball.get_rect()
        self.directionY = 1
        self.directionX = 1
        self.rand_dir = random.randint(0, 1)
        self.randY = random.randrange(5, self.screen_dims[1] - 5)
        self.pos = [self.screen_dims[0] // 2, self.randY]
        self.angle = 0
        self.pointA = 0
        self.pointB = 0

    def move(self):
        if self.rand_dir == 1:
            self.pos[0] += 3 * self.directionX
        else:
            self.pos[0] += -3 * self.directionX
        self.pos[1] += 3 * m.sin(m.radians(self.angle)) * self.directionY
        self.ball_r.center = (self.pos[0], self.pos[1])

        if self.pos[0] < 0:
            self.pos = [self.screen_dims[0] // 2, self.screen_dims[1] // 2]
            self.pointB += 1
        if self.pos[0] >= self.screen_dims[0]:
            self.pos = [self.screen_dims[0] // 2, self.screen_dims[1] // 2]
            self.pointA += 1
        if self.pos[1] <= 0 or self.pos[1] >= self.screen_dims[1]-10:
            self.directionY *= -1

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = [800, 800]
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.run = True
        self.paddleOne = Pong("paddle.png", [10, 350], self.WINDOW_SIZE)
        self.paddleTwo = Pong("paddle.png", [782, 350], self.WINDOW_SIZE)
        self.ball = Ball("ball.png", self.WINDOW_SIZE)
        self.line = pygame.image.load("dotted line.png").convert_alpha()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.paddleOne.movement[0] = True
                if event.key == pygame.K_s:
                    self.paddleOne.movement[1] = True
                if event.key == pygame.K_UP:
                    self.paddleTwo.movement[0] = True
                if event.key == pygame.K_DOWN:
                    self.paddleTwo.movement[1] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.paddleOne.movement[0] = False
                if event.key == pygame.K_s:
                    self.paddleOne.movement[1] = False
                if event.key == pygame.K_UP:
                    self.paddleTwo.movement[0] = False
                if event.key == pygame.K_DOWN:
                    self.paddleTwo.movement[1] = False

    def game_loop(self):
        while self.run:
            self.window.fill("black")
            self.handle_events()
            self.paddleOne.move()
            self.paddleTwo.move()
            self.ball.move()
            self.window.blit(self.ball.ball, self.ball.pos)
            self.window.blit(self.paddleOne.pong, self.paddleOne.pos)
            self.window.blit(self.paddleTwo.pong, self.paddleTwo.pos)
            self.window.blit(self.line, (-15, 0))
            if self.ball.ball_r.colliderect(self.paddleOne.pong_r) or self.ball.ball_r.colliderect(
                    self.paddleTwo.pong_r):
                self.ball.directionX *= -1
                self.ball.angle = random.randrange(-45, 45)
            font = pygame.font.Font("PixeloidMono-d94EV.ttf", 50)
            text = font.render(f" {self.ball.pointA}             {self.ball.pointB} ", True, "white")
            self.window.blit(
                text,
                (self.WINDOW_SIZE[0] // 2 - text.get_width() // 2, (self.WINDOW_SIZE[1]-750) - text.get_height() // 2)
            )
            pygame.display.update()
            self.clock.tick(80)





