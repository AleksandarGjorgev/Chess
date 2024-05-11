import pygame
import sys

# Innit 
pygame.init()

pygame.display.set_caption("Chess")

#Screen resoulution
width = 1200
height = 1000

screen = pygame.display.set_mode([width,height])

#Fonts
font = pygame.font.Font("freesansbold.ttf", 40)
big_font = pygame.font.Font("freesansbold.ttf", 60)

#Timer, fps
fps = 60
timer = pygame.time.Clock()
