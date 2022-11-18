
#code = '''
import pygame
import sys
sys.dont_write_bytecode = True
from scripts.colors import *
from scripts.pyscreen import *
from scripts.object import *
pygame.display.set_caption("pyautomata")
def moveTo(ax,ay,bx,by):
    try:
        steps_number = int(max(abs(bx-ax),abs(by-ay)))
        steps = []
        stepx = float(bx-ax)/steps_number
        stepy = float(by-ay)/steps_number
        for i in range(steps_number+1):
            steps.append([int(ax + stepx*i), int(ay + stepy*i)])
        return steps
    except:
        return []
createX = 0
createY = 0
rl = ""
uw = ""
clock = pygame.time.Clock()
inventory = True
mainMenu = True
while True:
    screen.t = pygame.time.get_ticks()
    screen.deltaTime = (screen.t - screen.getTicksLastFrame) / 1000.0
    screen.getTicksLastFrame = screen.t
    screen.screen.fill((125,125,125))
    mx, my = pygame.mouse.get_pos()
    mx -= screen.CAMPOS[0] + 12.5
    my -= screen.CAMPOS[1] + 12.5
    click = pygame.mouse.get_pressed()
    if(mainMenu==False):
        if(inventory==False):
            for i in screen.map:
                i.update()
            if(click[0]):
                if(screen.BRD==2):
                    r = 0
                    for i in screen.objects:
                        if(int(i.x/25) == int(mx/25) and int(i.y/25) == int(my/25)): screen.objects.pop(r)
                        r+=1
            for event in pygame.event.get():
                if(event.type==pygame.QUIT): sys.exit()
                if(event.type==pygame.MOUSEBUTTONDOWN):
                    spx = int(mx/50)*50
                    spy = int(my/50)*50
                    if(screen.BRD==1 and screen.CHOOSEN==1): createX,createY = mx, my
                    elif(screen.BRD==1 and screen.CHOOSEN==2): miner(spx,spy,screen.type)
                    elif(screen.BRD==1 and screen.CHOOSEN==3): seller(spx,spy)
                elif(event.type==pygame.MOUSEBUTTONUP):
                    if(screen.BRD==1 and screen.CHOOSEN==1):
                        if(int(createX/25) != int(mx/25) or int(createY/25) != int(my/25)):
                            line = moveTo(int(createX/25),int(createY/25),int(mx/25),int(my/25))
                            for i in line: object(i[0]*25,i[1]*25,colors.DARKGRAY)
                        else: object(int(mx/25)*25,int(my/25)*25,colors.DARKGRAY)
                        createY, createX = 0, 0
                if(event.type==pygame.KEYDOWN):
                    match event.key:
                        case pygame.K_e: screen.BRD = 1
                        case pygame.K_r: screen.BRD = 2
                        case pygame.K_y: screen.BRD = 0
                        case pygame.K_z: screen.TOWARD = 0
                        case pygame.K_x: screen.TOWARD = 1
                        case pygame.K_c: screen.TOWARD = 2
                        case pygame.K_v: screen.TOWARD = 3
                        case pygame.K_0: screen.CHOOSEN = 0
                        case pygame.K_1: screen.CHOOSEN = 1
                        case pygame.K_2: screen.CHOOSEN = 2
                        case pygame.K_3: screen.CHOOSEN = 3
                        case pygame.K_4: screen.CHOOSEN = 4
                        case pygame.K_5: screen.CHOOSEN = 5
                        case pygame.K_6: screen.CHOOSEN = 6
                        case pygame.K_7: screen.CHOOSEN = 7
                        case pygame.K_q: inventory = True
                    if(event.key==pygame.K_w): uw = "up"
                    elif(event.key==pygame.K_s): uw = "down"
                    if(event.key==pygame.K_a): rl = "left"
                    elif(event.key==pygame.K_d): rl = "right"
                elif(event.type==pygame.KEYUP):
                    if(event.key==pygame.K_w or event.key==pygame.K_s): uw = ""
                    if(event.key==pygame.K_a or event.key==pygame.K_d): rl = ""
            if(int(createX/25) != int(mx/25) or int(createY/25) != int(my/25)):
                if(createX!=0 and createY != 0):
                    line = moveTo(int(createX/25)*screen.scale,int(createY/25)*screen.scale,int(mx/25)*screen.scale,int(my/25)*screen.scale)
                    for i in line: pygame.draw.rect(screen.screen, "lightgray", pygame.Rect((i[0]*25+screen.CAMPOS[0])*screen.scale, (i[1]*25+screen.CAMPOS[1])*screen.scale, 25*screen.scale, 25*screen.scale))
            if(uw=="up"):
                screen.CAMPOS[1] += screen.playerSpeed * screen.deltaTime
                screen.PPOS[1] += screen.playerSpeed * screen.deltaTime
            elif(uw=="down"): 
                screen.CAMPOS[1] -= screen.playerSpeed * screen.deltaTime
                screen.PPOS[1] -= screen.playerSpeed * screen.deltaTime
            if(rl=="left"): 
                screen.CAMPOS[0] += screen.playerSpeed * screen.deltaTime
                screen.PPOS[0] += screen.playerSpeed * screen.deltaTime
            elif(rl=="right"): 
                screen.CAMPOS[0] -= screen.playerSpeed * screen.deltaTime
                screen.PPOS[0] -= screen.playerSpeed * screen.deltaTime
            r = 0
            for i in screen.objects: 
                if(i.alive==False):
                    screen.objects.pop(r)
                else:
                    i.update()
                r+=1
            pygame.draw.rect(screen.screen, "lightgray", pygame.Rect(int(mx/25)*25+screen.CAMPOS[0],int(my/25)*25+screen.CAMPOS[1], 25, 25))
            img = screen.font.render(screen.moves[screen.TOWARD-1], True, "black")

            screen.screen.blit(img, (0, screen.m.height-50))
            pygame.draw.rect(screen.screen, "red", pygame.Rect(screen.PPOS[0]-screen.CAMPOS[0],screen.PPOS[1]-screen.CAMPOS[1],60,60))
        else:
            for event in pygame.event.get():
                if(event.type==pygame.QUIT): sys.exit()
                if(event.type==pygame.KEYDOWN and event.key==pygame.K_q): inventory = False
            mouseRect = pygame.Rect(mx,my,1,1)
            color = ["black","blue","white","gold"]
            r = 0
            for i in color:
                objectRect = pygame.Rect(r*100,0,35,35)
                k = pygame.Rect.colliderect(mouseRect,objectRect)
                if(k):
                    screen.type = i
                    pygame.draw.rect(screen.screen,i, pygame.Rect(r*100,-5,56,56))
                pygame.draw.rect(screen.screen,i, objectRect)
                r+=1
        img = screen.font.render(str(screen.money), True, "black")
        screen.screen.blit(img,(screen.m.width/2,0))
    else:
        contorls = ["zxcv - rotating","e - build mode", "f - destroy mode","1 - conwayor belt", "2 - miner", "3 - seller", "q - inventory"]
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
        y = 0
        for i in contorls:
            img = screen.font.render(i, True, "black")
            screen.screen.blit(img, (0,screen.m.height-y*50))
            y += 1
        img = screen.font.render("Play", True, "black")
        screen.screen.blit(img, (screen.m.width/2-250,screen.m.height/2))
        rect = pygame.Rect(screen.m.width/2-250,screen.m.height/2,50,50)
        mouseRect = pygame.Rect(mx,my,1,1)
        if (pygame.Rect.colliderect(rect,mouseRect) and click[0]):
            mainMenu = False
    clock.tick()    
    fps = screen.font.render(str(clock.get_fps()), True, "Black")
    screen.screen.blit(fps,(0,0))
    pygame.display.flip()
#'''
#exec(code)