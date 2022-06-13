# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import sys
from sprites import player

pygame.init()

size = width, height = 320 * 4, 240 * 4
black = 0, 0, 0

screen = pygame.display.set_mode(size)

__up__ = 0
__down__ = 1
__left__ = 2
__right__ = 3

clock = pygame.time.Clock()

player_x = width / 2
player_y = height / 2

bg_x = - width / 2
bg_y = - height / 2
position_quantize_value_x = width / 32
position_quantize_value_y = height / 32

player_width = 64
player_height = 64
vel = 5

bg_area = 0

bg = [pygame.image.load('sourceimages/spring/grass01ax.png')]


def move_forward():
    global player_y, bg_y
    # player_y -= vel
    bg_y += vel
    player.is_moving = True
    player.direction = __up__


def move_backward():
    global player_y, bg_y
    # player_y += vel
    bg_y -= vel
    player.is_moving = True
    player.direction = __down__


def move_left():
    global player_x, bg_x
    # player_x -= vel
    bg_x += vel
    player.is_moving = True
    player.direction = __left__


def move_right():
    global player_x, bg_x
    # player_x += vel
    bg_x -= vel
    player.is_moving = True
    player.direction = __right__


def stop_moving():
    player.is_moving = False


def controls():
    if pygame.key.get_pressed()[pygame.K_w] and player_y > vel:
        move_forward()
    elif pygame.key.get_pressed()[pygame.K_s] and height - player_y > vel:
        move_backward()
    elif pygame.key.get_pressed()[pygame.K_a] and player_x > vel:
        move_left()
    elif pygame.key.get_pressed()[pygame.K_d] and width - player_x > vel:
        move_right()
    else:
        stop_moving()


def redraw_game_window():
    screen.fill(black)
    background = pygame.transform.scale(bg[bg_area], (width * 2, height * 2))
    screen.blit(background, (bg_x, bg_y))  # draw background

    if player.walk_count + 1 > 4 * player.frames:
        player.walk_count = 0

    if player.direction == __left__ and player.is_moving:
        screen.blit(player.walk_left[player.walk_count // player.frames], (player_x, player_y))
        player.walk_count += 1
    elif player.direction == __right__ and player.is_moving:
        screen.blit(player.walk_right[player.walk_count // player.frames], (player_x, player_y))
        player.walk_count += 1
    elif player.direction == __up__ and player.is_moving:
        screen.blit(player.walk_up[player.walk_count // player.frames], (player_x, player_y))
        player.walk_count += 1
    elif player.direction == __down__ and player.is_moving:
        screen.blit(player.walk_down[player.walk_count // player.frames], (player_x, player_y))
        player.walk_count += 1
    else:
        screen.blit(player.still[player.direction], (player_x, player_y))
    pygame.display.flip()


# main loop
run = True
while run:
    clock.tick(27)
    controls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(69)

    redraw_game_window()
