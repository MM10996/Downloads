import pygame
import random

# initialize pygame window size
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("Rock Paper Scissors")

# updates the game
clock = pygame.time.Clock()

# background
BACKGROUND = (255, 140, 205)
BUTTON_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.Font(None, 36)