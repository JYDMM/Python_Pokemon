# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import sys

pygame.init()

size = width, height = 320 * 4, 240 * 4
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

__forward__ = 'w'
__backward__ = 's'
__left__ = 'a'
__right__ = 'd'

player_x = width / 2
player_y = height / 2


def move_forward():
    global player_y
    player_y -= 1


def move_backward():
    global player_y
    player_y += 1


def move_left():
    global player_x
    player_x -= 1


def move_right():
    global player_x
    player_x += 1


def controls():
    if pygame.key.get_pressed()[pygame.K_w]:
        move_forward()
    if pygame.key.get_pressed()[pygame.K_s]:
        move_backward()
    if pygame.key.get_pressed()[pygame.K_a]:
        move_left()
    if pygame.key.get_pressed()[pygame.K_d]:
        move_right()


ball = pygame.image.load("unnamed.jpg")
ballrect = ball.get_rect()

while 1:
    controls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(69)
    screen.fill(black)
    ballrect.center = player_x, player_y
    screen.blit(ball, ballrect)
    pygame.display.flip()


# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
