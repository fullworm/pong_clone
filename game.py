import pygame
import random as r
pygame.init()

WINDOW_SIZE = [800, 800]
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pong1 = pygame.image.load("paddle.png").convert_alpha()
pong2 = pygame.image.load("paddle.png").convert_alpha()
ball = pygame.image.load("ball.png").convert_alpha()
pong1_r = pong1.get_rect()
pong2_r = pong2.get_rect()
ball_r = ball.get_rect()
movement = [False, False]
movement2 = [False, False]
pong1_pos = [20, 400]
pong2_pos = [770,400]
rand_y = r.randint(10,790)
rand_dir = r.randint(0,1)
ball_pos = [400, rand_y]
run: bool = True
direction = 1
while run:
    window.fill("black")
    if rand_dir == 1:
        ball_pos[0] += 3 * direction
    else:
        ball_pos[0] += -3 * direction
    if pong1_pos[1] < 0:
        pong1_pos[1] = 1
    elif pong1_pos[1] >= 715:
        pong1_pos[1] = 714
    else:
        pong1_pos[1] += (movement[1] - movement[0]) * 7
    if pong2_pos[1] < 0:
        pong2_pos[1] = 1
    elif pong2_pos[1] >= 715:
        pong2_pos[1] = 714
    else:
        pong2_pos[1] += (movement2[1] - movement2[0]) * 7
    if ball_pos[0] < 0 or ball_pos[0] >= WINDOW_SIZE[0]:
        ball_pos = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]
    window.blit(pong1, pong1_pos)
    pong1_r.center = pong1_pos
    window.blit(pong2,pong2_pos)
    pong2_r.center = pong2_pos
    window.blit(ball, ball_pos)
    ball_r.center = ball_pos
    if ball_r.colliderect(pong2_r) or ball_r.colliderect(pong1_r):
        direction *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement[0]= True
            if event.key == pygame.K_s:
                movement[1] = True
            if event.key == pygame.K_UP:
                movement2[0]= True
            if event.key == pygame.K_DOWN:
                movement2[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movement[0] = False
            if event.key == pygame.K_s:
                movement[1] = False
            if event.key == pygame.K_UP:
                movement2[0] = False
            if event.key == pygame.K_DOWN:
                movement2[1] = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()