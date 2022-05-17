# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import sys
from SpriteSheet import SpriteSheet

pygame.init()

size = width, height = 320 * 4, 240 * 4
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

__up__ = 0
__down__ = 1
__left__ = 2
__right__ = 3

clock = pygame.time.Clock()

player_x = width / 2
player_y = height / 2

trainer = "trainer.png"
sprite = SpriteSheet(trainer)

player_width = 64
player_height = 64
vel = 5
frames = 3
direction = __up__
walk_count = 0
is_moving = False

bg_area = 0

walk_left = [sprite.image_at((64 * 0, 64, 64 * 1, 128)),
             sprite.image_at((64 * 1, 64, 64 * 2, 128)),
             sprite.image_at((64 * 2, 64, 64 * 3, 128)),
             sprite.image_at((64 * 3, 64, 64 * 4, 128))]

walk_right = [sprite.image_at((64 * 0, 128, 64 * 1, 192)),
              sprite.image_at((64 * 1, 128, 64 * 2, 192)),
              sprite.image_at((64 * 2, 128, 64 * 3, 192)),
              sprite.image_at((64 * 3, 128, 64 * 4, 192))]

walk_down = [sprite.image_at((64 * 0, 0, 64 * 1, 64)),
             sprite.image_at((64 * 1, 0, 64 * 2, 64)),
             sprite.image_at((64 * 2, 0, 64 * 3, 64)),
             sprite.image_at((64 * 3, 0, 64 * 4, 64))]

walk_up = [sprite.image_at((64 * 0, 192, 64 * 1, 256)),
           sprite.image_at((64 * 1, 192, 64 * 2, 256)),
           sprite.image_at((64 * 2, 192, 64 * 3, 256)),
           sprite.image_at((64 * 3, 192, 64 * 4, 256))]

walk_still = [sprite.image_at((64 * 0, 192, 64 * 1, 256)),
              sprite.image_at((64 * 0, 0, 64 * 1, 64)),
              sprite.image_at((64 * 0, 64, 64 * 1, 128)),
              sprite.image_at((64 * 0, 128, 64 * 1, 192))]

bg = [pygame.image.load('sourceimages/spring/grass01ax.png')]


def move_forward():
    global player_y, direction, is_moving
    player_y -= vel
    is_moving = True
    direction = __up__


def move_backward():
    global player_y, direction, is_moving
    player_y += vel
    is_moving = True
    direction = __down__


def move_left():
    global player_x, direction, is_moving
    player_x -= vel
    is_moving = True
    direction = __left__


def move_right():
    global player_x, direction, is_moving
    player_x += vel
    is_moving = True
    direction = __right__


def stop_moving():
    global is_moving
    is_moving = False


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
    global walk_count, frames
    screen.fill(black)
    screen.blit(bg[bg_area], (0, 0))  # draw background

    if walk_count + 1 > 4 * frames:
        walk_count = 0

    if direction == __left__ and is_moving:
        screen.blit(walk_left[walk_count // frames], (player_x, player_y))
        walk_count += 1
    elif direction == __right__ and is_moving:
        screen.blit(walk_right[walk_count // frames], (player_x, player_y))
        walk_count += 1
    elif direction == __up__ and is_moving:
        screen.blit(walk_up[walk_count // frames], (player_x, player_y))
        walk_count += 1
    elif direction == __down__ and is_moving:
        screen.blit(walk_down[walk_count//frames], (player_x, player_y))
        walk_count += 1
    else:
        screen.blit(walk_still[direction], (player_x, player_y))
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
