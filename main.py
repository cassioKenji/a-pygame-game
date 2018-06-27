import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

black = (0,255,0)

# main loop
while True:
  screen.fill((255, 0, 0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # update

  # draw
  pygame.draw.lines(screen, black, False, [(100,500), (150,200), (200,100)], 1)

  pygame.display.update()
  fpsClock.tick(fps)
