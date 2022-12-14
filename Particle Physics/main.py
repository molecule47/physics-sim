import sys
import pygame
import pymunk
from pygame.locals import *
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

clock = pygame.time.Clock()

pygame.init()

windowSize = (1500, 800)
window = pygame.display.set_mode((windowSize), pygame.NOFRAME, vsync=1)

text_color = (255, 255, 255)

def mtext(text, font, text_color, x, y):
    m = font.render(text, True, text_color)
    window.blit(m, (x, y))


font = pygame.font.Font('fonts/C&C Red Alert [INET].ttf', 20)


def main():

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


main()
