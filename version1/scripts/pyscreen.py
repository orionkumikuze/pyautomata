import pygame
from screeninfo import get_monitors
class screen:
    for m in get_monitors():
        print(m)
    screen = pygame.display.set_mode((m.width,m.height))
    TOWARD = 1
    objects = []
    BRD = 0
    CAMPOS = [0,0]
    PPOS = [m.width/2,m.height/2]
    scale = 1
    CHOOSEN = 0
    moves = ["right","down","left","up"]
    pygame.font.init()
    font = pygame.font.Font("font.ttf",50)
    objectAmount = 0
    map = []
    type = "blue"
    getTicksLastFrame = 0
    playerSpeed = 525
    deltaTime = 1
    money = 0
    researchPoint = 0