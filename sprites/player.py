import pygame

__up__ = 0
__down__ = 1
__left__ = 2
__right__ = 3

frames = 3
direction = __up__
walk_count = 0

is_moving = False

walk_left = [pygame.image.load("sourceimages/Trainer/trainer_left_1.png"),
             pygame.image.load("sourceimages/Trainer/trainer_left_2.png"),
             pygame.image.load("sourceimages/Trainer/trainer_left_3.png"),
             pygame.image.load("sourceimages/Trainer/trainer_left_4.png")]

walk_right = [pygame.image.load("sourceimages/Trainer/trainer_right_1.png"),
              pygame.image.load("sourceimages/Trainer/trainer_right_2.png"),
              pygame.image.load("sourceimages/Trainer/trainer_right_3.png"),
              pygame.image.load("sourceimages/Trainer/trainer_right_4.png")]

walk_down = [pygame.image.load("sourceimages/Trainer/trainer_down_1.png"),
             pygame.image.load("sourceimages/Trainer/trainer_down_2.png"),
             pygame.image.load("sourceimages/Trainer/trainer_down_3.png"),
             pygame.image.load("sourceimages/Trainer/trainer_down_4.png")]

walk_up = [pygame.image.load("sourceimages/Trainer/trainer_up_1.png"),
           pygame.image.load("sourceimages/Trainer/trainer_up_2.png"),
           pygame.image.load("sourceimages/Trainer/trainer_up_3.png"),
           pygame.image.load("sourceimages/Trainer/trainer_up_4.png")]

still = [pygame.image.load("sourceimages/Trainer/trainer_up_1.png"),
         pygame.image.load("sourceimages/Trainer/trainer_down_1.png"),
         pygame.image.load("sourceimages/Trainer/trainer_left_1.png"),
         pygame.image.load("sourceimages/Trainer/trainer_right_1.png")]