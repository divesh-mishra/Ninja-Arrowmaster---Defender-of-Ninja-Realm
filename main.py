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
