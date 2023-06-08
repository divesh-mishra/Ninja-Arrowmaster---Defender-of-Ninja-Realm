import pygame
from sys import exit
from random import randint, choice

pygame.init()

# Creating Game Window
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("NINJA ARROWMASTER")
iconImg = pygame.image.load('ninja.png')
pygame.display.set_icon(iconImg)

background = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()
# tutorial screen

text_font = pygame.font.Font('Assets/font_space_n.otf', 30)
tutorial_font = pygame.font.Font('Assets/ShortBaby-Mg2w.ttf', 40)
tutorial_text1 = tutorial_font.render('1) Use Space-bar to jump.', True, 32)
tutorial_text2 = tutorial_font.render('2) Use Right key to shoot the arrow.', True, 32)
return_button = pygame.image.load('Assets/return_button.png')
return_rect = return_button.get_rect(center=(400, 400))
return_text = text_font.render('RETURN', True, 32)
return_text_rect = return_text.get_rect(center=(400, 400))

# Score
score_var = 0
score_values_list = [0]
# score_max = 0
if len(score_values_list) > 3:
    score_values_list.remove(min(score_values_list))

score_font = pygame.font.Font('Assets/ShortBaby-Mg2w.ttf', 40)


def score_board():
    score_surf = score_font.render(f'Score:{score_var}', True, 32)
    screen.blit(score_surf, (370, 10))
