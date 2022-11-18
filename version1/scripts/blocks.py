import pygame
from scripts.pyscreen import *
class block:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        screen.map.append(self)
    def update(self):
        pygame.draw.rect(screen.screen,self.color, pygame.Rect(self.x+screen.CAMPOS[0],self.y+screen.CAMPOS[1],25,25))
